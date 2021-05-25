import json
import time

from constants.request_model import RequestTest
from constants.request_model import RequestPostLogin
from constants.request_model import RequestPostCadastroPessoa
from constants.request_model import RequestPostPessoasList
from constants.request_model import RequestGetPessoa
from constants.request_model import RequestPostCadastroDisciplina
from constants.request_model import RequestPostDisciplinaList
from constants.request_model import RequestPostCadastroSerie
from constants.request_model import RequestPostSerieList
from constants.request_model import RequestPostCadastroPeriodoAcademico
from constants.request_model import RequestPostPeriodoAcademicoList
from constants.request_model import RequestPostCadastroTipoNota
from constants.request_model import RequestPostTipoNotaList
from constants.request_model import RequestPostCadastroHorario
from constants.request_model import RequestPostHorarioList
from constants.request_model import RequestPostCadastroModulo
from constants.request_model import RequestPostModuloList
from constants.request_model import RequestPostCadastroGrupo
from constants.request_model import RequestPostGrupoList
from constants.request_model import RequestPostErrorList
from constants.request_model import RequestPostAuditoriaList
from constants.request_model import BaseRequestModel
from constants.request_model import RequestGetLogDetail

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
from service.basic.grupo_service import GrupoService

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

@app.get("/get-pessoa")
def get_pessoa(data: RequestGetPessoa, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    return system.make_return_data(return_constants.STATUS_SUCCESS, {})

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

@app.post("/disciplina-list")
def get_disciplina_list( data: RequestPostDisciplinaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = DisciplinaService.list(data=data);
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

@app.post("/serie-list")
def get_serie_list( data: RequestPostSerieList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = SerieService.list(data=data);
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

@app.post("/periodo-academico-list")
def get_periodo_list( data: RequestPostPeriodoAcademicoList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PeriodoService.list(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/cadastro-tipo-nota")
def read_cadastro_tipo_nota( data: RequestPostCadastroTipoNota, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TipoNotaService.storeTipoNota(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)

@app.post("/tipo-nota-list")
def get_tipo_nota_list( data: RequestPostTipoNotaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TipoNotaService.list(data=data);
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

@app.post("/horario-list")
def get_horario_list( data: RequestPostHorarioList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = HorarioService.list(data=data);
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

@app.post("/modulo-list")
def get_modulo_list( data: RequestPostModuloList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = ModuloService.list(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-grupo")
def read_cadastro_grupo( data: RequestPostCadastroGrupo, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = GrupoService.storeGrupo(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)

@app.post("/grupo-list")
def get_grupo_list( data: RequestPostGrupoList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = GrupoService.list(data=data);
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
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = AuditoriaService.getAuditoriaList(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-permissions")
def get_permissions(data: BaseRequestModel, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()

        response = [
            'Home',
            'Cadastro Pessoa',
            'Cadastro Disciplina',
            'Cadastro Série',
            'Cadastro Período',
            'Cadastro Nota',
            'Cadastro Tipo de Nota',
            'Cadastro Horário',
            'Cadastro Módulo',
            'Erros',
            'Auditoria'
        ]

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-log-detail")
def get_log_detail(data: RequestGetLogDetail, request: Request):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        

        if not data.ref_error_id is None:
            erro = ErrorService.getError(data.ref_error_id)
            auditoria = AuditoriaService.getAuditoria(erro['ref_log_api'])
            session = SessionService.getSession(auditoria['ref_session'])
            pessoa = PessoaService.getPessoa(session['ref_pessoa'])
        elif not data.ref_auditoria_id is None:
            auditoria = AuditoriaService.getAuditoria(data.ref_auditoria_id)
            erro = ErrorService.getErrorByAuditoria(data.ref_auditoria_id)
            session = SessionService.getSession(auditoria['ref_session'])
            pessoa = PessoaService.getPessoa(session['ref_pessoa'])
        else:
            raise Exception("Ou o id de erro ou log deve ser informado")
        
        retorno = {
            'auditoria': auditoria,
            'erro': erro,
            'session': session,
            'pessoa': pessoa
        }
        print(retorno)
        return system.make_return_data(return_constants.STATUS_SUCCESS, retorno)
    except Exception as e:
        return system.make_error_return(e)