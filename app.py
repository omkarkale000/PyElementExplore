# app.py
import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
import pubchempy as pcp
import requests
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from io import BytesIO
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

def search_pubchem(compound: str) -> int:
    try:
        result = pcp.get_compounds(compound, 'name', record_type='3d')[0]
        return result.cid
    except (IndexError, pcp.PubChemHTTPError) as e:
        print(f"Error searching PubChem for {compound}: {e}")
        return None

def download_sdf(cid: int) -> str:
    try:
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF'
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except (requests.exceptions.RequestException, pcp.PubChemHTTPError) as e:
        print(f"Error downloading SDF for CID {cid}: {e}")
        return None

def sdf_to_base64_image(sdf_content: str) -> str:
    try:
        mol_3d = Chem.MolFromMolBlock(sdf_content)
        mol_2d = Chem.Mol(mol_3d)
        AllChem.Compute2DCoords(mol_2d)
        img = Draw.MolToImage(mol_2d)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except (ValueError, TypeError) as e:
        print(f"Error converting SDF to 2D: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('main_menu'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/main_menu')
def main_menu():
    return render_template('main_menu.html')

@app.route('/molecular_structure', methods=['GET', 'POST'])
def molecular_structure():
    if request.method == 'POST':
        compound_name = request.form['compound_name'].lower()

        # Handle special case for "hydrogen"
        if compound_name == "hydrogen":
            result = {
                "compound_name": compound_name,
                "error": f"Hydrogen is too simple, please choose a more complex compound."
            }
            return render_template('molecular_structure.html', result=result)

        cid = search_pubchem(compound_name)

        if cid is None:
            result = {"error": f"No CID found for {compound_name}"}
        else:
            sdf = download_sdf(cid)
            if sdf is None:
                result = {"error": f"Unable to download SDF for {compound_name}"}
            else:
                result = {
                    "compound_name": compound_name,
                    "sdf": sdf,
                    "image": sdf_to_base64_image(sdf)
                }

        return render_template('molecular_structure.html', result=result)
    return render_template('molecular_structure.html', result=None)

@app.route('/element_details')
def element_details():
    return render_template('element_details.html')

if __name__ == '__main__':
    app.run(debug=True)
