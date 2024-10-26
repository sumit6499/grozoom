from typing import Union
from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "hello from server"}


@app.get('/health-check')
async def check_health():
    return {"message": "Health check success"}


class BookModel(BaseModel):
    name: str
    author: str


@app.post('/create-book')
async def create_book(book_data: BookModel) -> dict:
    return {
        "book": book_data.name,
        "author": book_data.author
    }


@app.get('/get-headers',status_code=201)
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None)
):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content_type"] = content_type
    return request_header
