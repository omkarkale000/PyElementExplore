Setting Up Environment:
Clone the Repository:

bash
Copy code
git clone https://github.com/omkarkale000/Element_mixer.git
Clones your GitHub repository to your local machine.
Create and Activate Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Creates a virtual environment and activates it.
Install Dependencies:

bash
Copy code
pip install flask flask_sqlalchemy werkzeug
Installs required dependencies for the Flask application.
Initialize the Database:

bash
Copy code
python init_db.py
Initializes the SQLite database.
Running the Application:
Run Flask Application:

bash
Copy code
python app.py
Starts the Flask development server.
Open in Browser (Optional):

bash
Copy code
xdg-open http://127.0.0.1:5000/
Opens the application in the default web browser.
Development Workflow:
Add Changes to Staging:

bash
Copy code
git add .
Stages all changes for commit.
Commit Changes:

bash
Copy code
git commit -m "Your commit message"
Commits the staged changes with a meaningful message.
Push Changes to GitHub:

bash
Copy code
git push origin main
Pushes the committed changes to your GitHub repository.
