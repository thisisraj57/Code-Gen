python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/palindrome")
async def palindrome(request: Request):
    data = await request.json()
    word = data['word']
    result = {'is_palindrome': word == word[::-1]}
    return JSONResponse(content=result)