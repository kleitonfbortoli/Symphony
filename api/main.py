import json
# import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from service.basic.pessoa_service import PessoaService
from service.basic.nota_service import NotaService
from service.basic.periodo_service import PeriodoService
from service.basic.tipo_nota_service import TipoNotaService
from service.basic.serie_service import SerieService
from service.basic.disciplina_service import DisciplinaService
from service.basic.horario_service import HorarioService
from service.basic.error_service import ErrorService
from service.basic.auditoria_service import AuditoriaService
from service.basic.modulo_service import ModuloService

from service.login.session_service import SessionService
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
        system.validate_user()
        response = PessoaService.storePessoa(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)

@app.get("/")
def read_root():
    pass
    # return make_return_data(return_constants.STATUS_SUCCESS, {"Hello": "World"})

@app.post("/login")
def read_login( data: RequestPostLogin, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        token_access = SessionService.newLogin(email=data.email,password=data.password)
        system.token_access = token_access['token_access']
        system.validate_user()
        return system.make_return_data(return_constants.STATUS_SUCCESS, token_access)
    except Exception as e:
        return system.make_error_return(e)
        

@app.post("/cadastro-pessoa")
def read_cadastro_pessoa( data: RequestPostCadastroPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PessoaService.storePessoa(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        

@app.post("/cadastro-disciplina")
def read_cadastro_disciplina( data: RequestPostCadastroDisciplina, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = DisciplinaService.store(data=data);
        print(response)
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/cadastro-serie")
def read_cadastro_serie( data: RequestPostCadastroSerie, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = SerieService.storeSerie(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/cadastro-periodo-academico")
def read_cadastro_periodo( data: RequestPostCadastroPeriodoAcademico, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PeriodoService.storePeriodo(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)

# @app.post("/cadastro-nota")
# def read_cadastro_nota( data: RequestPostCadastroNota, request: Request ):
#     try:
#         system = SystemService(data=data, request=request)
#         system.validate_user()
#         response = NotaService.storeNota(data=data);
#         return system.make_return_data(return_constants.STATUS_SUCCESS, response)
#     except Exception as e:
#         if 'system' in locals() :
#             return system.make_error_return(e);
#         else:
#             return SystemService().make_default_error_returm(excecao=e, data=data, request=request)
        
@app.post("/cadastro-tipo-nota")
def read_cadastro_tipo_nota( data: RequestPostCadastroTipoNota, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TipoNotaService.storeTipoNota(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/cadastro-horario")
def read_cadastro_horario( data: RequestPostCadastroHorario, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = HorarioService.storeHorario(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-modulo")
def read_cadastro_modulo( data: RequestPostCadastroModulo, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = ModuloService.storeModulo(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/pessoas-list")
def get_pessoas_list( data: RequestPostPessoasList, request: Request ):
    print('passo')
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PessoaService.getPessoasList(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/erros-list")
def get_erros_list( data: RequestPostErrorList, request: Request ):
    print('passo')
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = ErrorService.getErrorList(data=data);
        print(response)
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/auditoria-list")
def get_auditoria_list( data: RequestPostAuditoriaList, request: Request ):
    print('passo')
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = AuditoriaService.getAuditoriaList(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-permissions")
def get_permissions(data: BaseRequestModel, request: Request ):
    print('passo')
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()

        response = [
            'Home',
            'Cadastro Pessoa',
            'Cadastro Disciplina',
            'Cadastro Série',
            'Cadastro Período'
        ]

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
    