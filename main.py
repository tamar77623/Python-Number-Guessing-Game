
import random

mynumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
randomchoice = random.choice(mynumber)

def selecting_numbers():
    time = 0

    while time < 3:
        userexpectation = int(input("Enter the number you expect: "))

        if userexpectation < 1 or userexpectation > 10:
            print("Please enter a number between 1 and 10")
            continue

        elif userexpectation == randomchoice:
            print(f"You won! The computer chose {randomchoice}")
            break

        else:
            time += 1

            if userexpectation < randomchoice:
                print("Too Low! Try again.")
            else:
                print("Too High! Try again.")

    else:
        print(f"Game Over! The number was {randomchoice}")

selecting_numbers()
