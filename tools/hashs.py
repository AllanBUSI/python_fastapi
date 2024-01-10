from argon2 import PasswordHasher

def hash(password):
    return PasswordHasher().hash(password)

def verify(hash, password):
    return PasswordHasher().verify(hash=hash, password=password)
