import random

# Initialize game variables
cup_water = 0
rocks_in_cup = 0
crow_thirst = 100
game_over = False

print("Welcome to 'The Crow and the Cup' Game!\n")
print("The crow is thirsty, and you need to stack rocks in the cup to raise the water level.")

while not game_over:
    print("\nOptions:")
    print("1. Stack a rock in the cup")
    print("2. Let the crow drink")
    print("3. Quit the game")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        added_water = random.randint(1, 5)
        cup_water += added_water
        rocks_in_cup += 1
        crow_thirst -= added_water
        print(f"You added {added_water} units of water to the cup. The crow's thirst is now {crow_thirst}.")
    elif choice == "2":
        if cup_water >= 20:
            print("The crow is happy and quenched its thirst! You win!")
            game_over = True
        else:
            print("The water level is too low for the crow to drink. Keep stacking rocks.")
    elif choice == "3":
        print("You quit the game. The crow is still thirsty.")
        game_over = True
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    # Check for crow's condition
    if crow_thirst <= 0:
        print("The crow's thirst reached zero. The crow is satisfied, and you win!")
        game_over = True
    elif rocks_in_cup >= 20:
        print("You've stacked enough rocks, but the crow is still thirsty. You didn't add enough water.")
        game_over = True

print("Thanks for playing 'The Crow and the Cup' Game!")
