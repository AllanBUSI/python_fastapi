import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
async def MiddleUser(username, password):
    array = []
    print("============",re.fullmatch(regex, username))
    if username is None or len(username) <= 4 or len(username) >= 254 or re.fullmatch(regex, username) is None:
        array.append("Username invalide")
    if password is None or len(password) <= 6 or len(password) >= 254:
        array.append("Password invalide")
        
    return array




