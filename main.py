from typing import Union
from fastapi import FastAPI, Form
from typing_extensions import Annotated

from tools import jwt 
from middleware import userMiddle
from data import database

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
    
    jwts = jwt.JwtSign({ "username": username })
    
    print(jwts)
    
    connect = database.connect()
    select = database.select(connect, '*', 'user', 'username = %s', (username,))    
        
    if len(select) == 0:
        database.insert(connect, 'user', 'username, password', '(%s, %s)', (username, password,))
        database.disconnect(connect)
    else:
        database.disconnect(connect)
        return  {"error": "l'utilisateur est déjà inscrit"}
    
    return  {"user": username, "jwt": jwts}

@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    array = await userMiddle.MiddleUser(username=username, password=password)
    print(array)
    if len(array) > 0:
        return { "error": array}
    
    jwts = jwt.JwtSign({ "username": username })
    
    print(jwts)
    
    connect = database.connect()
    select = database.select(connect, '*', 'user', 'username = %s', (username,))    
        
    if len(select) == 0:
        database.insert(connect, 'user', 'username, password', '(%s, %s)', (username, password,))
        database.disconnect(connect)
    else:
        database.disconnect(connect)
        return  {"error": "l'utilisateur est déjà inscrit"}
    
    return  {"user": username, "jwt": jwts}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}