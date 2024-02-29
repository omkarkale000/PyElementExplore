#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Start the Flask application
python app.py &

# Open the application in the default web browser
xdg-open http://127.0.0.1:5000/
