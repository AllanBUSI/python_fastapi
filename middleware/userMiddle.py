
async def MiddleUser(username, password):
    array = []
    if username is None or len(username) <= 4 or len(username) >= 254:
        array.append("Username invalide")
    if password is None or len(password) <= 6 or len(password) >= 254:
        array.append("Password invalide")
    return array