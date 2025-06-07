class TechnicalException(Exception):
     def __init__(self, message="Technical Error Occurred"):
      self.code = 340
      self.message = message
      super().__init__(message) 
    