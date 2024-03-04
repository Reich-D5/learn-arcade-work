import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3

    done = False

    while not done:
        if thirst > 4:
            print("You are thirsty.")
        if thirst > 6:
            print("You died of thirst!")
            done = True
            continue
        if camel_tiredness > 5:
            print("Your camel is getting tired.")
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
            continue
        if miles_traveled - natives_distance <= 0:
            print("The natives caught you!")
            done = True
            continue
        elif miles_traveled - natives_distance < 15:
            print("The natives are getting close!")

        print("\nA. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            done = True
            print("You have quit the game.")
            continue

        elif user_choice.upper() == "E":
            print(f"Miles traveled: {miles_traveled}")
            print(f"Drinks in canteen: {canteen_drinks}")
            print(f"The natives are {miles_traveled - natives_distance} miles behind you.")

        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print("Your camel is happy now.")
            natives_distance += random.randint(7, 14)

        elif user_choice.upper() == "C":
            miles_traveled += random.randint(10, 20)
            print(f"You traveled {miles_traveled} miles.")
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            natives_distance += random.randint(7, 14)

        elif user_choice.upper() == "B":
            miles_traveled += random.randint(5, 12)
            print(f"You traveled {miles_traveled} miles.")
            thirst += 1
            camel_tiredness += 1
            natives_distance += random.randint(7, 14)

        elif user_choice.upper() == "A":
            if canteen_drinks > 0:
                thirst = 0
                canteen_drinks -= 1
                print("You drank from your canteen.")
            else:
                print("Your canteen is empty!")

            if random.randint(1, 20) == 1:
                print("You found an oasis!")
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0

        if miles_traveled >= 200 and not done:
            print("Congratulations! You won!")
            done = True


if __name__ == "__main__":
    main()
