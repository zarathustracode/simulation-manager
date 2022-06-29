from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
  return "Endpoint for the simulation manager database"