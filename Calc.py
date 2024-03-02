print("Welcom to Python Calculator")
while True:
  while True:
    try:
      first_num = float(input("enter first number : "))
      break
    except ValueError:
      print("Enter a valid value")

  while True:
    try:
      op = input("enter a operation : ")
      if op in ("+",
                "-",
                "*",
                "/"):
        break
      else:
        raise ValueError
    except ValueError:
      print("Enter a valid operation")
  while True:
    try:
      second_num = float(input("enter a second number : "))
      if second_num == 0 and op == "/":
        raise ZeroDivisionError
      break
    except ValueError:
      print("Enter a valid vlue")
    except ZeroDivisionError:
      print("Cannot devid on 0 , please enter a valid vlue")

  match op:
    case "+":
      result = first_num + second_num
    case "-":
      result = first_num - second_num
    case "/":
      result = first_num / second_num
    case "*":
      result = first_num * second_num
    case _:
      result = None
  if result != None:
    print("the result is : " , result)
  else:
    print("unxpected error occure")

  repeat = input("do you want to perform another operation (Y/N) : ")
  if repeat == "N":
    break
  elif repeat == "Y":
    continue
  else:
    print("please enter a valid value")


print("exiting Python Calculator")

