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


# method to check if a number is prime
def is_prime(n):
	if n < 2:
		return False

	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# method to check if a number is perfect or not

def is_perfect(n):
	sum = 0

	for i in range(1, n):
		if n%i == 0:
			sum += i
	if sum == n:
		return True
	else:
		return False


def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d**length for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

def get_parity(n: int) -> str:
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