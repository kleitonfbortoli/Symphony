from peewee import *
from peewee import PostgresqlDatabase

db = PostgresqlDatabase('symphony', user='symphony', host='127.0.0.1')

class SymphonyModel(Model):
    class Meta:
        database = db

""" TABELAS DE CADASTRO BÁSICOS """
class Pais(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    uf = CharField(max_length='3', null='false')
    
class Estado(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    sigla = CharField(max_length='2',null='false')
    ref_pais = ForeignKeyField(Pais,backref='id', null='false')
    
class Cidade(SymphonyModel):
    id = AutoField
    nome = TextField(null='false')
    ref_estado = ForeignKeyField(Estado, backref='id', null='false')

class Pessoa(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    dt_nascimento = DateField()
    ref_cidade = ForeignKeyField(Cidade, backref='id', null='false')
    
""" TABELAS DE CADASTRO ACADÊMICOS """
class Curso(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    ch_total = IntegerField(null='false')   

class Contrato(SymphonyModel):
    id = AutoField()
    ref_pessoa = ForeignKeyField(Pessoa, backref='id', null='false')
    ref_curso = ForeignKeyField(Curso, backref='id', null='false')
    
class Disciplina(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    ch = IntegerField(null='false')

class Matriz_Curso(SymphonyModel):
    id = AutoField()
    ref_curso = ForeignKeyField(Curso, backref='id', null='false')
    ref_dsiciplina = ForeignKeyField(Disciplina, backref='id', null='false')
    
class Horario(SymphonyModel):
    id = AutoField()
    dia_semana=,,,,,,,,,,,,,,,,,,,,,