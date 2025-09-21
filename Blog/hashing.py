from passlib.context import CryptContext

class Hash():
    def bcrypt(password):
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)
