

class Calculator:
  def calculate(self, expression):
    if not expression:
      raise Exception("Empty expression")
    tokens = expression.split()
    if len(tokens) < 3:
      raise Exception("illegal expression")

    operator = ''
    result = 0 
    for token in tokens:
      if len(operator) == 0:
        operator = token
        if operator == '*':
          result = 1 
      else:
        if operator == '+':
          result = result + int(token)
        if operator == '*':
          result = result * int(token)
    return result
    #pass
