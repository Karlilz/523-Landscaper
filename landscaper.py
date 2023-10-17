money = 0
tools = ["teeth"]

def cut_grass(tool):
    global money  
    if tool == "teeth":
        money += 1
    elif tool == "scissors":
        money += 5
    elif tool == "push lawnmower":
        money += 50
    elif tool == "battery-powered lawnmower":
        money += 100
    elif tool == "team":
        money += 250

def buy_tool(tool, cost):
    global money  
    if tool not in tools and money >= cost:
        money -= cost
        tools.append(tool)

def hire_team():
    global money  
    if "team" not in tools and money >= 500:
        money -= 500
        tools.append("team")

def get_tool_cost(tool):
    if tool == "scissors":
        return 5
    elif tool == "push lawnmower":
        return 25
    elif tool == "battery-powered lawnmower":
        return 250
    else:
        return 0
    

while money < 1000:
    print(f"Money: ${money}")
    print(f"Tools: {', '.join(tools)}")

    action = input("What would you like to do? (cut/buy/hire/quit): ")

    if action == "cut":
        cut_grass(tools[-1])
    elif action == "buy":
        tool_to_buy = input("Which tool would you like to buy? (scissors/push lawnmower/battery-powered lawnmower): ")
        buy_tool(tool_to_buy, get_tool_cost(tool_to_buy))
    elif action == "hire":
        if "team" not in tools:
            print("You can only hire a team when you have the battery-powered lawnmower.")
        else:
            hire_team()
    elif action == "quit":
        break
    else:
        print("Invalid choice. Please choose a valid action.")


if money >= 1000:
    print("Congratulations! You've won the game!")
