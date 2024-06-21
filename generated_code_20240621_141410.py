python
from fastapi import FastAPI
from typing import List
app = FastAPI()

def check_palindrome(text: str):
    low = 0
    high = len(text) - 1
    flag = True

    while low <= high:
        if text[low] != text[high]:
            flag = False
            break
        low += 1
        high -= 1
    return flag

@app.post('/palindrome')
def is_palindrome(text: str):
    return {'is_palindrome': check_palindrome(text)}