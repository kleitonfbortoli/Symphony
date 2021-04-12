class SymphonyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class ForbidenException(Exception):
    def __init__(self, message):
        super().__init__(message)

class LoginException(Exception):
    def __init__(self, message):
        super().__init__(message)