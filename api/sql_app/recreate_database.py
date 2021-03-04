import database as database
from database import *

db.connect()

db.drop_tables([Pais,Estado,Cidade,Pessoa,Curso,Contrato])
db.create_tables([Pais,Estado,Cidade,Pessoa,Curso,Contrato]) 