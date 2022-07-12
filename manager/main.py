from fastapi import FastAPI
from database import User, Simulation, Model, Base
from database_setup import engine


Base.metadata.create_all(engine)



app = FastAPI()

@app.get('/')
def main():
  return "Endpoint for the simulation manager database"