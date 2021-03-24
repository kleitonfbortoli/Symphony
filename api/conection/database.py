from peewee import Model,AutoField,TextField,CharField,ForeignKeyField,IntegerField,DateField,DoubleField,BooleanField,PostgresqlDatabase

Symphony_Db = PostgresqlDatabase('symphony', user='symphony', password='carambolasAzuis784', host='localhost')

class SymphonyModel(Model):
    class Meta:
        database = Symphony_Db

""" TABELAS DE CADASTRO BÁSICOS """
class Pais(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    uf = CharField(max_length='3', null='false')
    
class Estado(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    sigla = CharField(max_length='2',null='false')
    ref_pais = ForeignKeyField(Pais,backref='cod', null='false')
    
class Cidade(SymphonyModel):
    cod = AutoField
    nome = TextField(null='false')
    ref_estado = ForeignKeyField(Estado, backref='cod', null='false')

class Pessoa(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    dt_nascimento = DateField()
    email = TextField()
    password = TextField()
    ref_cidade = ForeignKeyField(Cidade, backref='cod', null='false')
    
""" TABELAS DE CADASTRO ACADÊMICOS """
class Serie(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    ch_total = IntegerField(null='false')   

class Matricula_Serie(SymphonyModel):
    cod = AutoField()
    ref_pessoa = ForeignKeyField(Pessoa, backref='cod', null='false')
    ref_serie = ForeignKeyField(Serie, backref='cod', null='false')
    
class Disciplina(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    ch = IntegerField(null='false')

class Matriz_Serie(SymphonyModel):
    cod = AutoField()
    ref_serie = ForeignKeyField(Serie, backref='cod', null='false')
    ref_dsiciplina = ForeignKeyField(Disciplina, backref='cod', null='false')
    
class Tipo_Nota(SymphonyModel):
    cod = AutoField()
    descricao = TextField(null='false')

class Nota(SymphonyModel):
    cod = AutoField()
    descricao = TextField(null='false')
    ordem = IntegerField(null='false')
    ref_tipo_nota = ForeignKeyField(Tipo_Nota, backref='cod', null='false')
    ref_matriz_serie = ForeignKeyField(Matriz_Serie, backref='cod', null='false')
    
class Turma(SymphonyModel):
    cod = AutoField()
    ref_matriz_serie = ForeignKeyField(Matriz_Serie, backref='cod', null='false')
    
class Nota_Turma(SymphonyModel):
    cod = AutoField()
    descricao = TextField(null='false')
    ordem = IntegerField(null='false')
    ref_tipo_nota = ForeignKeyField(Tipo_Nota, backref='cod', null='false')
    ref_turma = ForeignKeyField(Turma, backref='cod', null='false')
    
class Avaliacao(SymphonyModel):
    cod = AutoField()
    nome = TextField(null='false')
    descricao = TextField()
    peso = IntegerField(null='false')
    ref_nota_turma = ForeignKeyField(Nota_Turma, backref='cod', null='false')
    
class Matricula_Turma(SymphonyModel):
    cod = AutoField()
    dt_matricula = DateField(null='false')
    ref_turma = ForeignKeyField(Turma, backref='cod', null='false')
    ref_matricula_serie = ForeignKeyField(Matricula_Serie, backref='cod', null='false')

class Horario(SymphonyModel):
    cod = AutoField()
    descricao = TextField(null='false')
    dia_semana = CharField(max_length='2',null='false')
    turno = CharField(max_length='2',null='false')
    hora_ini = TextField(null='false')
    hora_fim = TextField(null='false')
    
class Periodo_Academico(SymphonyModel):
    cod = AutoField()
    descricao = TextField(null='false')
    dt_inicio = DateField(null='false')
    dt_final = DateField(null='false')
    

class Turma_Ocorencia(SymphonyModel):
    cod = AutoField()
    ref_turma = ForeignKeyField(Turma, backref='cod', null='false')
    ref_horario = ForeignKeyField(Horario, backref='cod', null='false')
    ref_periodo_academico = ForeignKeyField(Periodo_Academico, backref='cod', null='false')
    
class Frequencia(SymphonyModel):
    cod = AutoField()
    presente = BooleanField(null='false')
    ref_matricula_turma = ForeignKeyField(Matricula_Turma, backref='cod', null='false')
    ref_turma_ocorrencia = ForeignKeyField(Turma_Ocorencia, backref='cod', null='false')
    
class Turma_Professor(SymphonyModel):
    cod = AutoField()
    ref_pessoa = ForeignKeyField(Pessoa, backref='cod', null='false')
    ref_turma = ForeignKeyField(Turma, backref='cod', null='false')
    
class Avaliacao_Matricula_Turma(SymphonyModel):
    cod = AutoField()
    valor = DoubleField(null='false')
    ref_avaliacao = ForeignKeyField(Avaliacao, backref='cod', null='false')
    ref_matricula = ForeignKeyField(Matricula_Turma, backref='cod', null='false')