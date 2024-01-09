from typing import Union
from fastapi import FastAPI, Form
from typing_extensions import Annotated
from middleware import userMiddle

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/register")
async def register_item(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    array = await userMiddle.MiddleUser(username=username, password=password)
    print(array)
    if len(array) > 0:
        return { "error": array}
    
    
    return  {"user": username}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}