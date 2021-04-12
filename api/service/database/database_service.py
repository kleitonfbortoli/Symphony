from peewee import Model
from pydantic import BaseModel

<<<<<<< HEAD
from database.symphony_db import *
=======
from database.database import *
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175

class DataBaseService:
    @staticmethod
    @Symphony_Db.atomic()
    def store(entity: Model, data: BaseModel):
        try:
            json_data = DataBaseService.convertBaseModelToJson(data)
            if(json_data['id']):
                entity.update(**json_data).where(entity.id == json_data['id']).execute()
            else:
<<<<<<< HEAD
                print(json_data)
                print(entity.create(**json_data))
        except Exception as e:
            print(str(e))
=======
                entity.create(**json_data)
        except:
            pass
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175
            
    @staticmethod
    def convertBaseModelToJson(data: BaseModel):
        json_data = json.loads(json.dumps(data.__dict__))
        return json_data
        