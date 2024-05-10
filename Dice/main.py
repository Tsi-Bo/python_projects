import random
def dice_roll(dice):
    roll = random.randint(1, dice)
    print(roll)

while True:
    choice = int(input("Chose your dice (100, 20, 12, 10, 8, 6, 4): "))
    if choice in [100, 20, 12, 10, 8, 6, 4]:
        dice_roll(choice)
    else: 
        print("Please chose a correct dice!")
    
