from fastapi import FastAPI

app = FastAPI()

@app.get('/bill')

def index():
    return {'message': 'Welcome to PSG College of Arts and Science, Coimbatore'}

