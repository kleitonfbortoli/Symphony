from pydantic import BaseModel, ValidationError, validator
import re 

email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

class BaseRequestModel(BaseModel):
    token_access: str

class RequestPostLogin(BaseModel):
    email: str
    password: str
    
    @validator('email')
    def valid_email(cls, v):
        if(not re.search(email_regex, v)):
            raise ValueError('O email fornecido é inválido')
        return v
    
class RequestPostCadastroDisciplina(BaseRequestModel):
    nome: str
    ch: str
    
class RequestPostCadastroPessoa(BaseRequestModel):
    email: str
    password: str
    nome: str
    dt_nascimento: str