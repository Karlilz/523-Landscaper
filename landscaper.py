earnings = 0  
scissors = False  

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

    print("You can cut the lawn with your teeth.")
    earnings += 1  

    choice = input("Do you want to continue cutting the lawn with teeth? (yes/no): ").lower()
    
    if choice == "no":
        break  

print(f"Your total earnings: ${earnings}")
