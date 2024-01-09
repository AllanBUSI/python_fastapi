import jwt

def JwtSign(obj):
    encoded_jwt = jwt.encode(obj, "secret", algorithm="HS256")
    return encoded_jwt
