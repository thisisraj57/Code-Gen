python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

@app.get("/is_prime/{number}")
async def is_prime(number: int):
    """
    This function checks if a given number is prime.

    Args:
        number: The number to check.
    
    Returns:
        A boolean value indicating whether the number is prime or not.
    """

    if number <= 1:
        raise HTTPException(status_code=400, detail="Number must be greater than 1")

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True