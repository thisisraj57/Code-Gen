python
# FastAPI Import
from fastapi import FastAPI, Request, HTTPException
# Other Imports
from typing import List
from uuid import UUID

app = FastAPI()

@app.post("/palindrome")
async def is_palindrome(request: Request):
    """
    This function checks if a string is a palindrome.
    """
    try:
        # Extract the string from the request
        data = await request.json()
        string = data["string"]

        # Check if the string is a palindrome
        is_palindrome = palindrome(string)

        return {"is_palindrome": is_palindrome}

    except (TypeError, ValueError, KeyError):
        raise HTTPException(status_code=400, detail="Invalid input.")

@app.post("/sync_example")
async def sync_example( request: Request):
    """
    This is a sync example
    """
    try:
        data = await request.json()
        string = data["string"]

       # Check if the string is a palindrome
        is_palindrome = palindrome(string)

        return {"is_palindrome": is_palindrome}

    except (TypeError, ValueError, KeyError):
        return HTTPException(status_code=400, detail="Invalid input.")

def palindrome(string: str) -> bool:
    """
    This function checks if a string is a palindrome.
    """

    # Convert the string to lowercase and remove all spaces
    string = string.lower().replace(" ", "")

    # Check if the string is the same forwards and backwards
    return string == string[::-1]