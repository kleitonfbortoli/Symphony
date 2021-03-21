from peewee import *
from peewee import PostgresqlDatabase

Symphony_Db = PostgresqlDatabase('symphony', user='symphony', password='carambolasAzuis784', host='database')

class SymphonyModel(Model):
    class Meta:
        database = Symphony_Db

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
    email = TextField()
    password = TextField()
    ref_cidade = ForeignKeyField(Cidade, backref='id', null='false')
    
""" TABELAS DE CADASTRO ACADÊMICOS """
class Serie(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    ch_total = IntegerField(null='false')   

class Matricula_Serie(SymphonyModel):
    id = AutoField()
    ref_pessoa = ForeignKeyField(Pessoa, backref='id', null='false')
    ref_serie = ForeignKeyField(Serie, backref='id', null='false')
    
class Disciplina(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    ch = IntegerField(null='false')

class Matriz_Serie(SymphonyModel):
    id = AutoField()
    ref_serie = ForeignKeyField(Serie, backref='id', null='false')
    ref_dsiciplina = ForeignKeyField(Disciplina, backref='id', null='false')
    
class Tipo_Nota(SymphonyModel):
    id = AutoField()
    descricao = TextField(null='false')

class Nota(SymphonyModel):
    id = AutoField()
    descricao = TextField(null='false')
    ordem = IntegerField(null='false')
    ref_tipo_nota = ForeignKeyField(Tipo_Nota, backref='id', null='false')
    ref_matriz_serie = ForeignKeyField(Matriz_Serie, backref='id', null='false')
    
class Turma(SymphonyModel):
    id = AutoField()
    ref_matriz_serie = ForeignKeyField(Matriz_Serie, backref='id', null='false')
    
class Nota_Turma(SymphonyModel):
    id = AutoField()
    descricao = TextField(null='false')
    ordem = IntegerField(null='false')
    ref_tipo_nota = ForeignKeyField(Tipo_Nota, backref='id', null='false')
    ref_turma = ForeignKeyField(Turma, backref='id', null='false')
    
class Avaliacao(SymphonyModel):
    id = AutoField()
    nome = TextField(null='false')
    descricao = TextField()
    peso = IntegerField(null='false')
    ref_nota_turma = ForeignKeyField(Nota_Turma, backref='id', null='false')
    
class Matricula_Turma(SymphonyModel):
    id = AutoField()
    dt_matricula = DateField(null='false')
    ref_turma = ForeignKeyField(Turma, backref='id', null='false')
    ref_matricula_serie = ForeignKeyField(Matricula_Serie, backref='id', null='false')

class Horario(SymphonyModel):
    id = AutoField()
    descricao = TextField(null='false')
    dia_semana = CharField(max_length='2',null='false')
    turno = CharField(max_length='2',null='false')
    hora_ini = TextField(null='false')
    hora_fim = TextField(null='false')
    
class Periodo_Academico(SymphonyModel):
    id = AutoField()
    descricao = TextField(null='false')
    dt_inicio = DateField(null='false')
    dt_final = DateField(null='false')
    

class Turma_Ocorencia(SymphonyModel):
    id = AutoField()
    ref_turma = ForeignKeyField(Turma, backref='id', null='false')
    ref_horario = ForeignKeyField(Horario, backref='id', null='false')
    ref_periodo_academico = ForeignKeyField(Periodo_Academico, backref='id', null='false')
    
class Frequencia(SymphonyModel):
    id = AutoField()
    presente = BooleanField(null='false')
    ref_matricula_turma = ForeignKeyField(Matricula_Turma, backref='id', null='false')
    ref_turma_ocorrencia = ForeignKeyField(Turma_Ocorencia, backref='id', null='false')
    
class Turma_Professor(SymphonyModel):
    id = AutoField()
    ref_pessoa = ForeignKeyField(Pessoa, backref='id', null='false')
    ref_turma = ForeignKeyField(Turma, backref='id', null='false')
    
class Avaliacao_Matricula_Turma(SymphonyModel):
    id = AutoField()
    valor = DoubleField(null='false')
    ref_avaliacao = ForeignKeyField(Avaliacao, backref='id', null='false')
    ref_matricula = ForeignKeyField(Matricula_Turma, backref='id', null='false')