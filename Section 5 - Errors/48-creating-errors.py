class RuntimeErrorWithCode(TypeError):
  """Exception raised when a specific error code is needed."""
  def __init__(self, message, code):
    super().__init__(f'Error code {code}: {message}')
    self.code = code


err = RuntimeErrorWithCode('An error happened.', 500)
# Doc can be used only if you have the triple quotes in the class
print(err.__doc__)

raise err