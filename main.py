from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/{number}')

def get_number(number):
	return {
	    "number": 371,
	    "is_prime": False,
	    "is_perfect": False,
	    "properties": ["armstrong", "odd"],
	    "digit_sum": 11, 
	    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
	}