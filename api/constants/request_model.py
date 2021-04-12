from pydantic import BaseModel, ValidationError, validator
import re 
import datetime
from typing import Optional

email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

""" Aqui obriga a todos os requests passarem o tokem_access que é a informação de quem está logado,
    os requests que não necessitam estar logado, usam direto BaseModel  """
class BaseRequestModel(BaseModel):
<<<<<<< HEAD
    token: str
=======
    token_access: str
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175

class RequestPostLogin(BaseModel):
    email: str
    password: str
<<<<<<< HEAD
    token: str
=======
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175
    
    @staticmethod
    @validator('email')
    def valid_email(cls, v):
        if(not re.search(email_regex, v)):
            raise ValueError('O email fornecido é inválido')
        return v
    
    # @validator('email')
    
class RequestTest(BaseModel):
    nome: str
    uf: str
    
class RequestPostCadastroDisciplina(BaseRequestModel):
    nome: str
    ch: str
    
class RequestPostCadastroPessoa(BaseRequestModel):
    id: Optional[int]
    email: str
    password: str
    nome: str
    dt_nascimento: str
    
    @staticmethod
    @validator('email')
    def valid_email(cls, v):
        if(not re.search(email_regex, v)):
            raise ValueError('O email fornecido é inválido')
        return v
    
    @staticmethod
    @validator('password')
    def valid_password(cls,v):
        passlenth = len(v)
        if(passlenth < 8 and passlenth > 16):
            raise ValueError('A senha informada deve possuir entre 8 e 16 caracteres')
        return v
    
    @staticmethod
    @validator('dt_nascimento')
    def validDate(cls,v):
        try:
            date1 = datetime.datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Formato de data incorreto, precisa ser YYYY-MM-DD")
        
        date2 = datetime.datetime.now();
        
        if(date1 > date2):
            raise ValueError("A data não pode ser maior que hoje")
        return v