earnings = 0  
scissors = False  
lawnmower = False  
battery_lawnmower = False  
team_hired = False  

while True:
    if not scissors:
        print(f"Current earnings: ${earnings}")
        buy_choice = input("Do you want to buy a pair of rusty scissors for $5? (yes/no): ").lower()
        if buy_choice == "yes" and earnings >= 5:
            earnings -= 5
            scissors = True
            print("You bought a pair of rusty scissors!")
        elif buy_choice == "yes":
            print("You don't have enough money to buy scissors.")
        elif buy_choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if scissors:
        choice = input("Do you want to cut the lawn with your rusty scissors? (yes/no): ").lower()
        if choice == "yes":
            earnings += 5  
            print(f"You earned $5. Your total earnings: ${earnings}")
        elif choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if not lawnmower and scissors:
        print(f"Current earnings: ${earnings}")
        buy_choice = input("Do you want to buy an old-timey push lawnmower for $25? (yes/no): ").lower()
        if buy_choice == "yes" and earnings >= 25:
            earnings -= 25
            lawnmower = True
            print("You bought an old-timey push lawnmower!")
        elif buy_choice == "yes":
            print("You don't have enough money to buy a lawnmower.")
        elif buy_choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if lawnmower:
        choice = input("Do you want to cut the lawn with your old-timey push lawnmower? (yes/no): ").lower()
        if choice == "yes":
            earnings += 50  
            print(f"You earned $50. Your total earnings: ${earnings}")
        elif choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if not battery_lawnmower and lawnmower:
        print(f"Current earnings: ${earnings}")
        buy_choice = input("Do you want to buy a fancy battery-powered lawnmower for $250? (yes/no): ").lower()
        if buy_choice == "yes" and earnings >= 250:
            earnings -= 250
            battery_lawnmower = True
            print("You bought a fancy battery-powered lawnmower!")
        elif buy_choice == "yes":
            print("You don't have enough money to buy a battery-powered lawnmower.")
        elif buy_choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if battery_lawnmower:
        choice = input("Do you want to cut the lawn with your fancy battery-powered lawnmower? (yes/no): ").lower()
        if choice == "yes":
            earnings += 100  
            print(f"You earned $100. Your total earnings: ${earnings}")
        elif choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if not team_hired and battery_lawnmower:
        print(f"Current earnings: ${earnings}")
        hire_choice = input("Do you want to hire a team of starving students for $500? (yes/no): ").lower()
        if hire_choice == "yes" and earnings >= 500:
            earnings -= 500
            team_hired = True
            print("You hired a team of starving students!")
        elif hire_choice == "yes":
            print("You don't have enough money to hire a team.")
        elif hire_choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    if team_hired:
        choice = input("Do you want to let your team of starving students cut the lawn? (yes/no): ").lower()
        if choice == "yes":
            earnings += 200  
            print(f"You earned $200. Your total earnings: ${earnings}")
        elif choice == "no":
            pass
        else:
            print("Please enter a valid choice (yes/no).")

    choice = input("Do you want to cut the lawn with your teeth? (yes/no): ").lower()

    if choice == "no":
        break  

print(f"Your total earnings: ${earnings}")
