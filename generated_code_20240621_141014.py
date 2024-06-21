python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

@app.get("/palindrome/{word}")
async def is_palindrome(word: str):
    """
    Checks if a given word is a palindrome.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """

    # Check if the word is empty or None
    if not word or word is None:
        raise HTTPException(status_code=400, detail="Invalid word")

    # Reverse the word
    reversed_word = word[::-1]

    # Check if the reversed word is the same as the original word
    if word == reversed_word:
        return True
    else:
        return False