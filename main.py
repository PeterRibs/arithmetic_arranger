import re

def arithmetic_arranger(problems, solve = False):

  if(len(problems)>5):
    return "Error: Too many problems."
    
  firstValue = ""
  secondValue = ""
  finalLines = ""
  result = ""
  finalString = ""
  
  for problem in problems:
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstNumber = problem.split()[0]
    operator = problem.split()[1]
    secondNumber = problem.split()[2]

    if (len(firstNumber) >= 5 or len(secondNumber) >= 5):
      return "Error: Numbers cannot be more than four digits."

    operation = ""
    if(operator == '+'):
      operation = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-"):
      operation = str(int(firstNumber) - int(secondNumber))

    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length-1)
    line = ""
    res = str(operation).rjust(length)
    for s in range(length):
      line += "-"

    if problem != problems[-1]:
      firstValue += top + '    '
      secondValue += bottom + '    '
      finalLines += line + '    '
      result += res + '    '
    else:
      firstValue += top
      secondValue += bottom
      finalLines += line
      result += res

  if solve:
    finalString = firstValue + "\n" + secondValue + "\n" + finalLines + "\n" + result
  else:
    finalString = firstValue + "\n" + secondValue + "\n" + finalLines
  return finalString