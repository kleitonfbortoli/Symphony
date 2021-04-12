import secrets
from uuid import uuid4
from datetime import date, datetime, timedelta
from database.symphony_db import Session, Symphony_Db
from service.basic.pessoa_service import PessoaService
from exceptions.SymphonyException import LoginException,ForbidenException

class SessionService:
    @staticmethod
    def getNewTokenAccess():
        uuid = str(uuid4())
        hex_id = secrets.token_hex()
        
        token = uuid + hex_id
        
        return token
    
    @staticmethod
    def isLoged(token):
        date = datetime.now() - timedelta(hours = 3)
        session = Session.select().where(Session.token == token, Session.access_time >= date, Session.logout_time.is_null()).first()

        if session is None:
            raise ForbidenException(message="Usuário não logado")
        else:
            return session
    
    @staticmethod
    @Symphony_Db.atomic()
    def newLogin(email: str, password: str):
        token = SessionService.getNewTokenAccess();
        pessoa = PessoaService.getByEmailAndSenha(email, password)

        if pessoa is None:
            raise LoginException(message="Usuário ou senha incorretos")
        else:
            session = Session(ref_pessoa=pessoa,token=token)
            session.save()
            return token
        