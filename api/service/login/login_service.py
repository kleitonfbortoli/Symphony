import secrets
from uuid import uuid4

class LoginService:
    @staticmethod
    def getNewTokenAccess():
        uuid = str(uuid4())
        hex_id = secrets.token_hex()
        
        token = uuid + hex_id
        
        return token
    
    @staticmethod
    def isLoged(token):
        pass
    
    @staticmethod
    def newLogin(email: str):
        pass