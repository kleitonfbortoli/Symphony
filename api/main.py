import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service.pessoa_service import *

# from sql_app.database import *
from base_model import *
from return_status import return_constants as return_constants

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

def make_return(status, response):
    return {"status":status, "response":response}

@app.get("/")
def read_root():
    return make_return(return_constants.STATUS_SUCCESS, {"Hello": "World"})

@app.post("/login")
def read_login( request: RequestPostLogin ):
    return make_return(return_constants.STATUS_SUCCESS, request)

@app.post("/cadastro-pessoa")
def read_cadastro_pessoa( request: RequestPostCadastroPessoa ):
    # pessoa = Pessoa(RequestPostCadastroPessoa)
    # print(pessoa)
    return make_return(return_constants.STATUS_SUCCESS, request)

@app.post("/cadastro-disciplina")
def read_cadastro_disciplina( request: RequestPostCadastroDisciplina ):
    retorno = Disciplina(nome='asdasd', ch='asdsad')
    retorno.save()
    return make_return(return_constants.STATUS_SUCCESS, retorno)