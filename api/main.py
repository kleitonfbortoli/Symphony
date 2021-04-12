import json
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from service.basic.pessoa_service import PessoaService
from service.login.session_service import SessionService
from service.log.error import ErrorService
from service.system.system_service import SystemService

from constants.request_model import *
from constants.status_model import return_constants as return_constants

from database.symphony_db import *

from exceptions.SymphonyException import *

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/teste1")
def teste1():
    app.a = "a"
    time.sleep(5)
    print(app.a)

@app.post("/teste2")
def teste2():
    app.a = "b"

@app.get("/recreate")
def recreateDatabase():
    Symphony_Db.drop_tables([Log_Error,Log_Api,Session,Avaliacao_Matricula_Turma,Turma_Professor,Frequencia,Turma_Ocorencia,Periodo_Academico,Horario,Matricula_Turma,Avaliacao,Nota_Turma,Turma,Nota,Tipo_Nota,Matriz_Serie,Disciplina,Matricula_Serie,Pessoa,Serie,Cidade,Estado,Pais])
    Symphony_Db.create_tables([Pais,Estado,Cidade,Pessoa,Serie,Matricula_Serie,Disciplina,Matriz_Serie,Tipo_Nota,Nota,Turma,Nota_Turma,Avaliacao,Matricula_Turma,Horario,Periodo_Academico,Turma_Ocorencia,Frequencia,Turma_Professor,Avaliacao_Matricula_Turma,Session,Log_Api,Log_Error]) 

@app.post("/teste")
def read_logina( data: RequestTest, request: Request):
    try:
        system = SystemService(data=data, request=request)
        response = PessoaService.storePessoa(data=request);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e);

@app.get("/")
def read_root():
    return make_return_data(return_constants.STATUS_SUCCESS, {"Hello": "World"})

@app.post("/login")
def read_login( data: RequestPostLogin, request: Request ):
    try:
        token = SessionService.newLogin(email=data.email,password=data.password)
        data.token = token
        system = SystemService(data=data, request=request)
        return system.make_return_data(return_constants.STATUS_SUCCESS, data)
    except LoginException as e:
        print(e)
    except Exception as e:
        print(e)
        # return system.make_error_return(e);
        

@app.post("/cadastro-pessoa")
def read_cadastro_pessoa( data: RequestPostCadastroPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        response = PessoaService.storePessoa(data=request);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e);
        

@app.post("/cadastro-disciplina")
def read_cadastro_disciplina( data: RequestPostCadastroDisciplina, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        
        # return system.make_return_data(return_constants.STATUS_SUCCESS, retorno)
    except Exception as e:
        return system.make_error_return(e);