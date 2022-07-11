# simulation-manager

Manage usage of computational resources for different users, machine learning models and data sets. 

# Run

To run the app execute

`uvicorn manager.main:app --host=0.0.0.0 --reload`

# Testing

To test the app run

`pytest manager/database.py`