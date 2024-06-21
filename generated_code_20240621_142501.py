python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.post("/palindrom_string")
async def create_items(request: Request):
    data = await request.json()
    string = data["string"]
    is_palindrome = string == string[::-1]
    response = {"is_palindrome": is_palindrome}
    return JSONResponse(content=jsonable_encoder(response))