from pydantic import BaseModel
import sys
sys.path.append("../")
from conection.database import *
class PessoaService:
    def storePessoa(RequestPostCadastroPessoa: BaseModel):
        # Symphony_Db.connect();
        try:
            pessoa = Pessoa(RequestPostCadastroPessoa)
            pessoa.save()
            # Symphony_Db.commit
            return "Registro salvo com sucesso"
        except Exception as e:
            # Symphony_Db.rollback
            raise e