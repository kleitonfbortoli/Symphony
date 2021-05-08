from peewee import Model,TextField,CharField,ForeignKeyField,IntegerField,DateField,DoubleField,BooleanField,PostgresqlDatabase,DateTimeField
from playhouse.postgres_ext import JSONField
from playhouse.postgres_ext import PostgresqlExtDatabase
import json
Symphony_Db = PostgresqlExtDatabase('symphony', user='symphony', password='carambolasAzuis784', host='localhost')

class SymphonyModel(Model):
    class Meta:
        database = Symphony_Db

""" TABELAS DE CADASTRO BÁSICOS """
class Pais(SymphonyModel):
    nome = TextField()
    uf = CharField(max_length='3')


class Estado(SymphonyModel):
    nome = TextField()
    sigla = CharField(max_length='2')
    ref_pais = ForeignKeyField(Pais)

class Cidade(SymphonyModel):
    nome = TextField()
    ref_estado = ForeignKeyField(Estado)

class Pessoa(SymphonyModel):
    nome = TextField()
    dt_nascimento = DateField()
    email = TextField()
    password = TextField()
    # ref_cidade = ForeignKeyField(Cidade)

""" TABELAS DE CADASTRO ACADÊMICOS """
class Serie(SymphonyModel):
    nome = TextField()
    ch_total = IntegerField()   

class Matricula_Serie(SymphonyModel):
    ref_pessoa = ForeignKeyField(Pessoa)
    ref_serie = ForeignKeyField(Serie)

class Disciplina(SymphonyModel):
    nome = TextField()
    ch = IntegerField()

class Matriz_Serie(SymphonyModel):
    ref_serie = ForeignKeyField(Serie)
    ref_disciplina = ForeignKeyField(Disciplina)

class Tipo_Nota(SymphonyModel):
    descricao = TextField()

class Nota(SymphonyModel):
    descricao = TextField()
    ordem = IntegerField()
    ref_tipo_nota = ForeignKeyField(Tipo_Nota)
    ref_matriz_serie = ForeignKeyField(Matriz_Serie)

class Turma(SymphonyModel):
    ref_matriz_serie = ForeignKeyField(Matriz_Serie)

class Nota_Turma(SymphonyModel):
    descricao = TextField()
    ordem = IntegerField()
    ref_tipo_nota = ForeignKeyField(Tipo_Nota)
    ref_turma = ForeignKeyField(Turma)

class Avaliacao(SymphonyModel):
    nome = TextField()
    descricao = TextField()
    peso = IntegerField()
    ref_nota_turma = ForeignKeyField(Nota_Turma)

class Matricula_Turma(SymphonyModel):
    dt_matricula = DateField()
    ref_turma = ForeignKeyField(Turma)
    ref_matricula_serie = ForeignKeyField(Matricula_Serie)

class Horario(SymphonyModel):
    descricao = TextField()
    dia_semana = TextField()
    turno = TextField()
    hora_ini = TextField()
    hora_fim = TextField()

class Periodo_Academico(SymphonyModel):
    descricao = TextField()
    dt_inicio = DateField()
    dt_final = DateField()

class Turma_Ocorencia(SymphonyModel):
    ref_turma = ForeignKeyField(Turma)
    ref_horario = ForeignKeyField(Horario)
    ref_periodo_academico = ForeignKeyField(Periodo_Academico)

class Frequencia(SymphonyModel):
    fl_presente = BooleanField()
    ref_matricula_turma = ForeignKeyField(Matricula_Turma)
    ref_turma_ocorrencia = ForeignKeyField(Turma_Ocorencia)

class Turma_Professor(SymphonyModel):
    ref_pessoa = ForeignKeyField(Pessoa)
    ref_turma = ForeignKeyField(Turma)

class Avaliacao_Matricula_Turma(SymphonyModel):
    valor = DoubleField()
    ref_avaliacao = ForeignKeyField(Avaliacao)
    ref_matricula = ForeignKeyField(Matricula_Turma)
 
    
""" TABELAS DE CONTROLE DE ACESSOS """
class Session(SymphonyModel):
    access_time = DateTimeField(default='now()')
    logout_time = DateTimeField(null="false")
    token = TextField()
    ref_pessoa = ForeignKeyField(Pessoa)

class Log_Api(SymphonyModel):
    ref_session = ForeignKeyField(Session, null=True)
    api_name = TextField()
    success = BooleanField()
    input_data = JSONField()
    output_data = JSONField()
    start_time = DateTimeField()
    end_time = DateTimeField()

class Log_Error(SymphonyModel):
    ref_session = ForeignKeyField(Session, null=True)
    ref_log_api = ForeignKeyField(Log_Api)
    time_error = DateTimeField(default='now()')
    error_message = TextField()

class Modulo(SymphonyModel):
    title = TextField()

class Grupo(SymphonyModel):
    descricao = TextField()

class Modulo_Grupo(SymphonyModel):
    ref_grupo = ForeignKeyField(Grupo)
    ref_modulo = ForeignKeyField(Modulo)

class Grupo_Usuario(SymphonyModel):
    ref_grupo = ForeignKeyField(Grupo)
    ref_pessoa = ForeignKeyField(Pessoa)
