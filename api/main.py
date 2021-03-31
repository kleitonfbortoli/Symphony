import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.basic.pessoa_service import *
from constants.request_model import *
from constants.status_model import return_constants as return_constants
from database.database import *

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

def make_return_data(status, response):
    return {"status":status, "response":response}

@app.post("/teste")
def read_logina( request: RequestTest ):
    json1 = json.loads(json.dumps(request.__dict__))
    pessoa = Pais.update(uf='BRA',nome='Brasil').where(Pais.id == 8).execute()
    print(pessoa)
    return make_return_data(return_constants.STATUS_SUCCESS, request)

@app.get("/")
def read_root():
    return make_return_data(return_constants.STATUS_SUCCESS, {"Hello": "World"})

@app.post("/login")
def read_login( request: RequestPostLogin ):
    return make_return_data(return_constants.STATUS_SUCCESS, request)

@app.post("/cadastro-pessoa")
def read_cadastro_pessoa( request: RequestPostCadastroPessoa ):
    PessoaService.storePessoa(data=request);
    return make_return_data(return_constants.STATUS_SUCCESS, request)

@app.post("/cadastro-disciplina")
def read_cadastro_disciplina( request: RequestPostCadastroDisciplina ):
    retorno = Disciplina(nome='asdasd', ch='asdsad')
    retorno.save()
    return make_return_data(return_constants.STATUS_SUCCESS, retorno)