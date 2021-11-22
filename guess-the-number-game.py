import random
random_number = random.randint(0, 1000) # This generates a random number between 0 and 1000
chances_given = 10 # This is the count of chances given, if the attempts exceeds the number of chances the game gets over.
attempts = 0 # These are the attempts made, after each attempt this number would be incremented by 1.

print("You have to guess a number between 0 and 1000.\nYou have 10 attempts.\nAfter every attempt, you get an "
      "hint such as guess a smaller number.\nIf you guess the number correctly in 10 attempt, you win.\n\n Good Luck!!!")

guessed_no = int(input("guess a number between 0 and 1000!!! -> "))
attempts += 1
print(f"\nYou have {chances_given - attempts} attempts left")

while True:
    if guessed_no == random_number:
        print("\nCongratulations, You Won!!!")
        break

    elif attempts == chances_given:
        print(f"\nYou lost... The number was {random_number}!!! Better luck next time...")
        break

    elif guessed_no > random_number:
        guessed_no = int(input("\nGuess a smaller number!!! -> "))
        attempts += 1
        print(f"\nYou have {chances_given - attempts} attempts left")
        continue

    else:
        guessed_no = int(input("\nGuess a larger number!!! -> "))
        attempts += 1
        print(f"\nYou have {chances_given - attempts} attempts left")
        continue

input("\nPress enter to exit")