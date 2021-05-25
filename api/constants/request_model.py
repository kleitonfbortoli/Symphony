from pydantic import BaseModel, ValidationError, validator, Json
import re 
import datetime
from typing import Optional



email_regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

""" Aqui obriga a todos os requests passarem o tokem_access que é a informação de quem está logado,
    os requests que não necessitam estar logado, usam direto BaseModel  """
class BaseRequestModel(BaseModel):
    id: Optional[int]
    token_access: str

class RequestPostLogin(BaseRequestModel):
    email: str
    password: str
    
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
    
class RequestPostCadastroSerie(BaseRequestModel):
    nome: str
    ch_total: str
    
class RequestPostCadastroPeriodoAcademico(BaseRequestModel):
    descricao: str
    dt_inicio: str
    dt_final: str
    
class RequestPostCadastroTipoNota(BaseRequestModel):
    descricao: str
    
class RequestPostCadastroHorario(BaseRequestModel):
    descricao: str
    dia_semana: str
    turno: str
    hora_ini: str
    hora_fim: str
    
class RequestPostCadastroModulo(BaseRequestModel):
    title: str
    
class RequestPostCadastroGrupo(BaseRequestModel):
    descricao: str
    
class BasicListRequest(BaseRequestModel):
    page_number: int
    page_size: int    
class RequestPostPessoasList(BasicListRequest):
    nome: Optional[str]
    email: Optional[str]
    
class RequestPostErrorList(BasicListRequest):
    error_message: Optional[str]
    
class RequestPostAuditoriaList(BasicListRequest):
    api_name: Optional[str]
    
class RequestPostDisciplinaList(BasicListRequest):
    nome: Optional[str]

class RequestPostSerieList(BasicListRequest):
    nome: Optional[str]
    ch_total: Optional[int]

class RequestPostPeriodoAcademicoList(BasicListRequest):
    descricao: Optional[str]

class RequestPostTipoNotaList(BasicListRequest):
    descricao: Optional[str]

class RequestPostHorarioList(BasicListRequest):
    descricao: Optional[str]
    dia_semana: Optional[str]
    turno: Optional[str]

class RequestPostModuloList(BasicListRequest):
    title: Optional[str]
    
class RequestPostGrupoList(BasicListRequest):
    descricao: Optional[str]

class RequestGetPessoa(BaseRequestModel):
    id: int
    
class RequestGetLogDetail(BaseRequestModel):
    ref_error_id: Optional[str]
    ref_auditoria_id: Optional[str]
    