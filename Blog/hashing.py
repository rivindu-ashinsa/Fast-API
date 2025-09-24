from passlib.context import CryptContext

ct =  CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password):
        return ct.hash(password)
    def verify(user_pw, request_pw):
        return ct.verify(request_pw, user_pw)