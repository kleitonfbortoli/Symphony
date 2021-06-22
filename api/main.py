import json
from service.basic.turma_service import TurmaService
import time
import requests

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
from service.basic.grupo_usuario_service import GrupoUsuarioService
from service.basic.matriz_service import MatrizService
from service.basic.matricula_service import MatriculaService
from service.basic.turma_ocorrencia_service import TurmaOcorrenciaService
from service.basic.turma_professor_service import TurmaProfessorService
from service.basic.turma_horario_service import TurmaHorarioService

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
    return PessoaService.get(1)

@app.get("/teste2")
def teste2():
    Symphony_Db.drop_tables([Turma_Professor])
    Symphony_Db.create_tables([Turma_Professor])
    

@app.get("/recreate")
def recreateDatabase():
    # Symphony_Db.drop_tables(
    #     [
    #         # Log_Error,
    #         # Log_Api,
    #         # Session,
    #         Avaliacao_Matricula,
    #         Turma_Professor,
    #         Frequencia,
    #         Turma_Ocorencia,
    #         Periodo,
    #         Horario,
    #         Matricula,
    #         Avaliacao,
    #         Nota,
    #         Matriz,
    #         Turma,
    #         Tipo_Nota,
    #         Disciplina,
    #         # Pessoa,
    #         Serie,
    #         Cidade,
    #         Estado,
    #         Pais,
    #         # Grupo_Usuario,
    #         # Modulo_Grupo,
    #         # Grupo,
    #         # Modulo
    #     ]
    # )
    Symphony_Db.create_tables(
        [
            Pais,
            Estado,
            Cidade,
            Pessoa,
            Serie,
            Disciplina,
            Matriz,
            Tipo_Nota,
            Nota,
            Turma,
            Avaliacao,
            Matricula,
            Horario,
            Turma_Horario,
            Periodo,
            Turma_Ocorencia,
            Frequencia,
            Turma_Professor,
            Avaliacao_Matricula,
            Session,
            Log_Api,
            Log_Error,
            Modulo,
            Grupo,
            Grupo_Usuario,
            Modulo_Grupo
        ]
    ) 

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
    
@app.get('/get-temperature')
def get_temperature():
    x = requests.get('https://api.hgbrasil.com/weather?woeid=457466&format=json').json()
    return x['results']

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
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PessoaService.getsList(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)

@app.post("/get-pessoa")
def get_pessoa(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = PessoaService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/cadastro-disciplina")
def read_cadastro_disciplina( data: RequestPostCadastroDisciplina, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = DisciplinaService.store(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-disciplina")
def get_disciplina(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = DisciplinaService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/disciplina-list")
def get_disciplina_list( data: RequestPostDisciplinaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = DisciplinaService.list(data=data);
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
    
@app.post("/get-serie")
def get_serie(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = SerieService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/serie-list")
def get_serie_list( data: RequestPostSerieList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = SerieService.list(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
        
@app.post("/cadastro-periodo")
def read_cadastro_periodo( data: RequestPostCadastroPeriodo, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = PeriodoService.storePeriodo(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-periodo")
def get_periodo(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = PeriodoService.get(data.id);
    print(response['id'])
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/periodo-list")
def get_periodo_list( data: RequestPostPeriodoList, request: Request ):
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
    
@app.post("/get-tipo-nota")
def get_tipo_nota(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = TipoNotaService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/tipo-nota-list")
def get_tipo_nota_list( data: RequestPostTipoNotaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TipoNotaService.list(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-turma")
def read_cadastro_turma( data: RequestPostCadastroTurma, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaService.store(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-turma")
def get_turma(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = TurmaService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/turma-list")
def get_turma_list( data: RequestPostTurmaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaService.list(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-nota")
def read_cadastro_nota( data: RequestPostCadastroNota, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = NotaService.store(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-nota")
def get_nota(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = NotaService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

@app.post("/nota-list")
def get_nota_list( data: RequestPostNotaList, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = NotaService.list(data=data);
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

@app.post("/get-horario")
def get_horario(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = HorarioService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

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
    
@app.post("/get-modulo")
def get_modulo(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = ModuloService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

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

@app.post("/get-grupo")
def get_grupo(data: RequestgetEntity, request: Request):
    system = SystemService(data=data, request=request)
    system.validate_user()
    response = GrupoService.get(data.id);
    return system.make_return_data(return_constants.STATUS_SUCCESS, response)

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
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = ErrorService.getErrorList(data=data);
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
            'Cadastro Grupo',
            'Cadastro Turma',
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
            pessoa = PessoaService.get(session['ref_pessoa'])
        elif not data.ref_auditoria_id is None:
            auditoria = AuditoriaService.getAuditoria(data.ref_auditoria_id)
            erro = ErrorService.getErrorByAuditoria(data.ref_auditoria_id)
            session = SessionService.getSession(auditoria['ref_session'])
            pessoa = PessoaService.get(session['ref_pessoa'])
        else:
            raise Exception("Ou o id de erro ou log deve ser informado")
        
        retorno = {
            'auditoria': auditoria,
            'erro': erro,
            'session': session,
            'pessoa': pessoa
        }
        return system.make_return_data(return_constants.STATUS_SUCCESS, retorno)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/grupo-list-by-pessoa")
def get_grupo_list_by_pessoa( data: RequestPostGrupoListByPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = GrupoUsuarioService.listGroupByPessoa(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/grupo-livre-list-by-pessoa")
def get_grupo_livre_list_by_pessoa( data: RequestPostGrupoListLivreByPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = GrupoUsuarioService.listGroupLivreByPessoa(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-grupo-na-pessoa")
def cadastro_grupo_na_pessoa( data: RequestPostCadastroGrupoNaPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = GrupoUsuarioService.saveGrupoNaPessoa(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-grupo-na-pessoa")
def delete_grupo_na_pessoa( data: RequestPostDeleteGrupoNaPessoa, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = GrupoUsuarioService.deleteGrupoNaPessoa(data=data);
        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-all-tipo-nota")
def get_all_tipo_nota(data: BaseRequestModel, request: Request):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TipoNotaService.getAll();

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-all-serie")
def get_all_serie(data: BaseRequestModel, request: Request):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = SerieService.getAll();

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-all-periodo")
def get_all_periodo(data: BaseRequestModel, request: Request):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = PeriodoService.getAll();

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/list-disciplina-by-serie")
def list_disciplina_by_serie( data: RequestPostDisciplinaListBySerie, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = MatrizService.ListDiciplinaBySerie(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-disciplina-livre-by-serie")
def get_disciplina_livre_by_serie( data: RequestPostDisciplinaLivreListBySerie, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = MatrizService.listDisciplinaLiveBySerie(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-matriz")
def cadastro_matriz( data: RequestPostCadastroMatriz, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = MatrizService.store(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-matriz")
def delete_matriz( data: RequestPostDeleteMatriz, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = MatrizService.delete(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/list-pessoa-by-turma")
def list_pessoa_by_turma( data: RequestPostPessoaListByTurma, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = MatriculaService.ListPessoaByTurma(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-pessoa-livre-by-turma")
def get_pessoa_livre_by_turma( data: RequestPostPessoaLivreListByTurma, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = MatriculaService.listPessoaLiveByTurma(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-matricula")
def cadastro_matricula( data: RequestPostCadastroMatricula, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = MatriculaService.store(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-matricula")
def delete_matricula( data: RequestPostDeleteMatricula, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = MatriculaService.delete(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
    
@app.post("/list-disciplina-by-turma")
def list_disciplina_by_turma( data: RequestPostDisciplinaListByTurma, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaOcorrenciaService.ListDisciplinaByTurma(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-disciplina-livre-by-turma")
def get_disciplina_livre_by_turma( data: RequestPostDisciplinaLivreListByTurma, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaOcorrenciaService.listDisciplinaLivreByTurma(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-turma-ocorrencia")
def cadastro_turma_ocorrencia( data: RequestPostCadastroTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaOcorrenciaService.store(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-turma-ocorrencia")
def delete_turma_ocorrencia( data: RequestPostDeleteTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaOcorrenciaService.delete(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/list-professor-by-turma-ocorrencia")
def list_professor_by_turma_ocorrencia( data: RequestPostProfessorListByTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaProfessorService.ListProfessorByTurmaOcorrencia(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-professor-livre-by-turma-ocorrencia")
def get_professor_livre_by_turma_ocorrencia( data: RequestPostProfessorLivreListByTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaProfessorService.listProfessorLivreByTurmaOcorrencia(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-turma-professor")
def cadastro_turma_professor( data: RequestPostCadastroTurmaProfessor, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaProfessorService.store(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-turma-professor")
def delete_turma_professor( data: RequestPostDeleteTurmaProfessor, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaProfessorService.delete(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/list-horario-by-turma-ocorrencia")
def list_horario_by_turma_ocorrencia( data: RequestPostHorarioListByTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaHorarioService.ListHorarioByTurmaOcorrencia(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/get-horario-livre-by-turma-ocorrencia")
def get_horario_livre_by_turma_ocorrencia( data: RequestPostHorarioLivreListByTurmaOcorrencia, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        response = TurmaHorarioService.listHorarioLivreByTurmaOcorrencia(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/cadastro-turma-horario")
def cadastro_turma_horario( data: RequestPostCadastroTurmaHorario, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaHorarioService.store(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)
    
@app.post("/delete-turma-horario")
def delete_turma_horario( data: RequestPostDeleteTurmaHorario, request: Request ):
    try:
        system = SystemService(data=data, request=request)
        system.validate_user()
        
        response = TurmaHorarioService.delete(data=data);

        return system.make_return_data(return_constants.STATUS_SUCCESS, response)
    except Exception as e:
        return system.make_error_return(e)