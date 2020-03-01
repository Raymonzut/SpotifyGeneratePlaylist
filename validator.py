from abc import ABC

class Validator(ABC):
  """Base class for executing checks on foreign object
  
  Usage
  -----
  Extend this class and add methods ending with 'check' as the name
  Use self.obj to get the foreign object
  """
  def __init__(self, obj):
    """Execute the provided checks on the foreign object"""
    self.obj = obj
    self.execute_checks()
    super().__init__()

  def execute_checks(self):
    """Loads all methods ending with 'check' and executes them"""
    # load methods
    methods = [m for m in dir(self) if m.endswith('check')]

    # execute them
    for method in methods:
      getattr(self, method)()
