print("Hello are you ready to play a geuss game !!")
print("tab [x] for exit")
while True:
  num = input("enter a number : ")
  if num == "x":
    print("Closing game")
    break

  try :
    num = int(num)
    if num % 2 == 0:
      print("This number is : Even")
    else:
      print("This number is : Odd")
  except ValueError:
    print("Please enter a valid number")

  word = input("Do you wanna to continue (Y/N) : ")
  if word == "y":
    continue
  else:
    print("exiting game......")
    break
