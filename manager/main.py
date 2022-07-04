from fastapi import FastAPI
import database

app = FastAPI()

@app.get('/')
def main():
  return "Endpoint for the simulation manager database"