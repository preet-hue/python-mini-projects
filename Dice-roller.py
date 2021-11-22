import random

while True:
    dice_no = random.randint(1, 6)
    if dice_no == 1:
        print("   \n 0 \n   ")
    elif dice_no == 2:
        print("  0\n   \n0  ")
    elif dice_no == 3:
        print("0  \n 0 \n  0")
    elif dice_no == 4:
        print("0 0\n   \n0 0")
    elif dice_no == 5:
        print("0 0\n 0 \n0 0")
    else:
        print("0 0\n0 0\n0 0")

    close_or_restart = input("Spin again? enter y for yes and n for no").lower()

    if close_or_restart == "y":
        continue
    elif close_or_restart == "n":
        break
    else:
        print("Incorrect value!!! spinning again!!!")
        continue

input("Press Enter to exit")
