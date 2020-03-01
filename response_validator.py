from validator import Validator
from exceptions import ResponseException


class ResponseValidator(Validator):
  """
  Implements Validator class 
  Adds check methods for response object
  """
  def status_code_check(self):
    """check for valid response status (200)"""
    if self.obj.status_code != 200:
        raise ResponseException(self.obj.status_code)
