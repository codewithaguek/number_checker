from fastapi import FastAPI, Query, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    if n < 2:
        return False
    divisors = [i for i in range(1, abs(n)) if n % i == 0]
    return sum(divisors) == abs(n)

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n: int) -> int:
    """Calculate the sum of digits of a number."""
    return sum(int(d) for d in str(abs(n)))

def get_parity(n: int) -> str:
    """Check if a number is odd or even."""
    return "odd" if n % 2 else "even"

def get_fun_fact(n: int) -> str:
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "No fun fact available."

@app.get("/api/classify-number")
async def classify_number(number: int = Query(..., description="The number to classify")):
    if not isinstance(number, int):
        raise HTTPException(status_code=400, detail={"number": str(number), "error": True})

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append(get_parity(number))

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number),
    }
    return response
