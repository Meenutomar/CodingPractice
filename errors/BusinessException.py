class BusinessException(Exception):
   
   def __init__(self, message=" Business Error Occurred"):
      self.code = 400
      self.message = message
      super().__init__(message) 


class YearException(BusinessException):
   def __init__(self, message="Invalid year"):
      self.code = 405
      self.message = message

