#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install Flask Flask-SQLAlchemy Werkzeug pytz pubchempy pandas rdkit requests

# Start the Flask application
python app.py

# Open the application in the default web browser
xdg-open http://127.0.0.1:5000/
