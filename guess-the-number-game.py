import random

random_number = random.randint(0, 1000)


guessed_no = int(input("guess a number between 0 and 1000!!! -> "))
while True:
    if guessed_no == random_number:
        print("Congratulations, You Won!!!")
        break
    elif guessed_no > random_number:
        guessed_no = int(input("Guess a smaller number!!! -> "))
        continue
    else:
        guessed_no = int(input("Guess a larger number!!! -> "))
        continue
