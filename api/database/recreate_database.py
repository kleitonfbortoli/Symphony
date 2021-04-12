# import database as database
<<<<<<< HEAD:api/database/recreate_database.py
from database.symphony_db import *
=======
from database.database import *
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175:api/sql_app/recreate_database.py

Symphony_Db.connect()

Symphony_Db.drop_tables([Avaliacao_Matricula_Turma,Turma_Professor,Frequencia,Turma_Ocorencia,Periodo_Academico,Horario,Matricula_Turma,Avaliacao,Nota_Turma,Turma,Nota,Tipo_Nota,Matriz_Serie,Disciplina,Matricula_Serie,Serie,Pessoa,Cidade,Estado,Pais])
Symphony_Db.create_tables([Pais,Estado,Cidade,Pessoa,Serie,Matricula_Serie,Disciplina,Matriz_Serie,Tipo_Nota,Nota,Turma,Nota_Turma,Avaliacao,Matricula_Turma,Horario,Periodo_Academico,Turma_Ocorencia,Frequencia,Turma_Professor,Avaliacao_Matricula_Turma]) 