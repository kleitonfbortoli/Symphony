# from peewee import Model,TextField,CharField,ForeignKeyField,IntegerField,DateField,DoubleField,BooleanField,PostgresqlDatabase,DateTimeField,
# import json
# Symphony_Db = PostgresqlDatabase('symphony', user='symphony', password='carambolasAzuis784', host='database')

# class SymphonyModel(Model):
#     class Meta:
#         database = Symphony_Db

# """ TABELAS DE CADASTRO BÁSICOS """
# class Pais(SymphonyModel):
#     nome = TextField(null='false')
#     uf = CharField(max_length='3', null='false')


# class Estado(SymphonyModel):
#     nome = TextField(null='false')
#     sigla = CharField(max_length='2',null='false')
#     ref_pais = ForeignKeyField(Pais, null='false')
    
# class Cidade(SymphonyModel):
#     nome = TextField(null='false')
#     ref_estado = ForeignKeyField(Estado, null='false')

# class Pessoa(SymphonyModel):
#     nome = TextField(null='false')
#     dt_nascimento = DateField()
#     email = TextField()
#     password = TextField()
#     ref_cidade = ForeignKeyField(Cidade, null='false')
    
# """ TABELAS DE CADASTRO ACADÊMICOS """
# class Serie(SymphonyModel):
#     nome = TextField(null='false')
#     ch_total = IntegerField(null='false')   

# class Matricula_Serie(SymphonyModel):
#     ref_pessoa = ForeignKeyField(Pessoa, null='false')
#     ref_serie = ForeignKeyField(Serie, null='false')
    
# class Disciplina(SymphonyModel):
#     nome = TextField(null='false')
#     ch = IntegerField(null='false')

# class Matriz_Serie(SymphonyModel):
#     ref_serie = ForeignKeyField(Serie, null='false')
#     ref_disciplina = ForeignKeyField(Disciplina, null='false')
    
# class Tipo_Nota(SymphonyModel):
#     descricao = TextField(null='false')

# class Nota(SymphonyModel):
#     descricao = TextField(null='false')
#     ordem = IntegerField(null='false')
#     ref_tipo_nota = ForeignKeyField(Tipo_Nota, null='false')
#     ref_matriz_serie = ForeignKeyField(Matriz_Serie, null='false')
    
# class Turma(SymphonyModel):
#     ref_matriz_serie = ForeignKeyField(Matriz_Serie, null='false')
    
# class Nota_Turma(SymphonyModel):
#     descricao = TextField(null='false')
#     ordem = IntegerField(null='false')
#     ref_tipo_nota = ForeignKeyField(Tipo_Nota, null='false')
#     ref_turma = ForeignKeyField(Turma, null='false')
    
# class Avaliacao(SymphonyModel):
#     nome = TextField(null='false')
#     descricao = TextField()
#     peso = IntegerField(null='false')
#     ref_nota_turma = ForeignKeyField(Nota_Turma, null='false')
    
# class Matricula_Turma(SymphonyModel):
#     dt_matricula = DateField(null='false')
#     ref_turma = ForeignKeyField(Turma, null='false')
#     ref_matricula_serie = ForeignKeyField(Matricula_Serie, null='false')

# class Horario(SymphonyModel):
#     descricao = TextField(null='false')
#     dia_semana = CharField(max_length='2',null='false')
#     turno = CharField(max_length='2',null='false')
#     hora_ini = TextField(null='false')
#     hora_fim = TextField(null='false')
    
# class Periodo_Academico(SymphonyModel):
#     descricao = TextField(null='false')
#     dt_inicio = DateField(null='false')
#     dt_final = DateField(null='false')
    

# class Turma_Ocorencia(SymphonyModel):
#     ref_turma = ForeignKeyField(Turma, null='false')
#     ref_horario = ForeignKeyField(Horario, null='false')
#     ref_periodo_academico = ForeignKeyField(Periodo_Academico, null='false')
    
# class Frequencia(SymphonyModel):
#     presente = BooleanField(null='false')
#     ref_matricula_turma = ForeignKeyField(Matricula_Turma, null='false')
#     ref_turma_ocorrencia = ForeignKeyField(Turma_Ocorencia, null='false')
    
# class Turma_Professor(SymphonyModel):
#     ref_pessoa = ForeignKeyField(Pessoa, null='false')
#     ref_turma = ForeignKeyField(Turma, null='false')
    
# class Avaliacao_Matricula_Turma(SymphonyModel):
#     valor = DoubleField(null='false')
#     ref_avaliacao = ForeignKeyField(Avaliacao, null='false')
#     ref_matricula = ForeignKeyField(Matricula_Turma, null='false')
    
    
# """ TABELAS DE CONTROLE DE ACESSOS """
# class Session(SymphonyModel):
#     access_time = DateTimeField()
#     logout_time = DateTimeField()
#     ref_pessoa = ForeignKeyField(Pessoa, null='false')

# class Log_Api(SymphonyModel):
#     ref_session = ForeignKeyField(Session, null='false')
#     api_name = TextField()
#     success = BooleanField()
#     input_data = JSONField()
#     output_data = JSONField()
#     start_time = DateTimeField()
#     end_time = DateTimeField()

# class Log_Error(SymphonyModel):
#     ref_session = ForeignKeyField(Session, null='false')
#     time_error = DateTimeField(default='now()')
#     error_json = JSONField()
#     error_message = TextField()