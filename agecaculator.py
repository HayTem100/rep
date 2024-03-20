print("#" * 80)
print("[you can write first letter of or full name of the time unite]".center(80, "#"))
print("#" * 80)
while True:

    age = int(input("Whats your age?: "))
    time_unite = input("Choose your time unite: Months, Weeks, Days: ").strip().lower()

    months = age * 12
    weeks = months * 4
    days = age * 365

    if time_unite == "months" or time_unite == "m":
        print(f"You have lived for {months:,} months.")
    elif time_unite == "weeks" or time_unite == "w":
        print(f"You have lived for {weeks:,} weeks.")
    elif time_unite == "days" or time_unite == "d":
        print(f"You have lived for {days:,} days.")
    else:
        print("Wrong choice!")
        
    x = input("Do you want to performe another age calculation [Y/N]: ").strip().lower()
    if x == "y":
        continue
    elif x == "n":
        print("end")
        break
    else:
        print("Invalid choice")
    
    


    