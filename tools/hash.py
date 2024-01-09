from argon2 import PasswordHasher

def hash(password):
    return PasswordHasher().hash(password)
