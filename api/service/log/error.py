from database.symphony_db import Session, Symphony_Db, Log_Error
import json


class ErrorService:
    
    @staticmethod
    @Symphony_Db.atomic()
    def logError(error: Exception, session: Session):
        json_error = json.dumps(error)
        message_error = str(error)
        logError = Log_Error(ref_session = session, erro_json = json_error, error_message = message_error)
        logError.save()