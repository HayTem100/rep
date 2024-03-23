while True:
  print("######################################################")
  print("############[Rock, Paper, Scissors]###################")
  print("######################################################")
  list = ["Anna","Nina","Sukuna"]
  name = input("Welcome to the game please enter your name : ").capitalize().strip()
  if name in list:
    print(f"Welcome {name} to the game")
  else:
    print(f"Sorry you are not allowed to play this game {name}")
    exit()

  begin = input("Press enter to begin or help to see the rules: ").strip().lower()
  if begin == "help" or begin == "h":
    print("""
     ****************Rules*********************
     * 1) You choose and the computer chooses *
     * 2) Rock smashes Scissors -> Rock wins  *
     * 3) Scissors cut Paper -> Scissors win  *
     * 4) Paper covers Rock -> Paper wins     *
     ******************************************
  """)

  else:
    print("#############[Let's start the game]#################")

  import random
  user_choice = input("Enter your choice (rock, paper, scissors): ")
  possible_choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(possible_choices)
  print(f"-You chose {user_choice},computer chose {computer_choice}.")
  if user_choice == computer_choice:
      print(f"-Both players selected {user_choice}. It's a tie!")

  elif user_choice == "rock":
      if computer_choice == "scissors":
        print("* Rock smashes scissors ! You win !")

      else:
        print("* Paper covers rock ! You lose.")

  elif user_choice == "paper":
    if computer_choice == "rock":
        print("* Paper covers rock ! You win !")

    else:
        print("* Scissors cuts paper ! You lose.")
  elif user_choice == "scissors":
    if computer_choice == "paper":
        print("* Scissors cuts paper ! You win !")

    else:
        print("*Rock smashes scissors ! You lose.")

  elif user_choice not in possible_choices:
    print("* Invalid choice. Please run the program again and choose rock, paper, or scissors.")

  print(f"-Thanks for playing {name}")
  print("="*50)

  play_again = input("==> Play again[Y/N]: ").strip().lower()
  if play_again == "yes" or play_again == "y":
    continue
  else:
    print("Thanks for playing")
    break


print("########################################################")
print("#####################Game Over##########################")
print("########################################################")

