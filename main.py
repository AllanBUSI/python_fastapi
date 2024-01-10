from typing import Union
from fastapi import FastAPI, Form
from typing_extensions import Annotated

from tools import jwt, hashs, sendEmail
from middleware import userMiddle
from data import database


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/register")
async def register_item(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    array = await userMiddle.MiddleUser(username=username, password=password)

    if len(array) > 0:
        return { "error": array}
    
    jwts = jwt.JwtSign({ "username": username })
        
    connect = database.connect()
    select = database.select(connect, '*', 'user', 'username = %s', (username,))    
        
    if len(select) == 0:
        database.insert(connect, 'user', 'username, password', '(%s, %s)', (username, hashs.hash(password),))
        database.disconnect(connect)
    else:
        database.disconnect(connect)
        return  {"error": "l'utilisateur est déjà inscrit"}
    
    return  {"user": username, "jwt": jwts}

@app.post("/login")
async def login_item(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    array = await userMiddle.MiddleUser(username=username, password=password)
    if len(array) > 0:
        return { "error": array}
    
    jwts = jwt.JwtSign({ "username": username })
        
    connect = database.connect()
    select = database.select(connect, '*', 'user', 'username = %s', (username,))    
    
    if len(select) == 0:
        return  {"error": "Username / Password invalide"}
    
    sendEmail.SendEmail(username)
    
    try: 
        verify = hashs.verify(hash=select[0][2], password=password)
    except Exception as e:
        return  {"error": "Username / Password invalide"}
    
    if verify == False:
        return  {"error": "Username / Password invalide"}

    return  {"user": username, "jwt": jwts}
    



@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}