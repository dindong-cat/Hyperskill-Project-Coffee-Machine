# Write your code here

water = 400
milk = 540  #540
beans = 120
cups = 9
money = 550
current_ingredient = [water, milk, beans, cups]


def check_material(choice):
    global money
    list = []
    espresso = [250, 0, 16, 1]
    latte = [350, 75, 20, 1]
    cappuccino = [200, 100, 12, 1]
    if choice == 1:
        required = espresso
    elif choice == 2:
        required = latte
    elif choice == 3:
        required = cappuccino
    for i in range(0, len(current_ingredient)):
        if current_ingredient[i] >= required[i]:
            list.append(i)
    if len(list) == 4:
        if choice == 1:
            money += 4
        if choice == 2:
            money += 7
        if choice == 3:
            money += 6
        for i in range(0, len(current_ingredient)):
            current_ingredient[i] -= required[i]
        print("I have enough resources, making you a coffee!")
        print()
    else:
        if 0 not in list:
            print("Sorry, not enough water!")
        elif 1 not in list:
            print("Sorry, not enough milk!")
        elif 2 not in list:
            print("Sorry, not enough beans!")
        elif 3 not in list:
            print("Sorry, not enough cups!")
        print()


def buy():
    global money
    print()
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == "1" or choice == "2" or choice == "3":
        choice = int(choice)
        check_material(choice)



def fill():
    print()
    add_water = int(input("Write how many ml of water do you want to add:\n"))
    current_ingredient[0] += add_water
    add_milk = int(input("Write how many ml of milk do you want to add:\n"))
    current_ingredient[1] += add_milk
    add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    current_ingredient[2] += add_beans
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    current_ingredient[3] += add_cups


def take():
    global money
    print(f"I gave you ${money}")
    print()
    money = 0
    return money


def display_message():
    print()
    print(f"""The coffee machine has:
    {current_ingredient[0]} of water
    {current_ingredient[1]} of milk
    {current_ingredient[2]} of coffee beans
    {current_ingredient[3]} of disposable cups
    ${money} of money""")
    print()


def start_working():
    while True:
        intention = input("Write action (buy, fill, take, remaining, exit):\n")
        if intention == "buy":
            buy()
        elif intention == "fill":
            fill()
        elif intention == "take":
            take()
        elif intention == "remaining":
            display_message()
        elif intention == "exit":
            break

start_working()
