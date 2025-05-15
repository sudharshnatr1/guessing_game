import random

def guess(number,level):
    for i in range(level):
        guess=int(input(f"guess the number you have {level-i} attempts left: "))
        if guess==number:
            print("you win")
            exit()
        elif guess>number:
            print("too high")
        elif guess<number:
            print("too low" )
    print("you lose")
    print(f"the number was {number}")

print("welcome to the number guessing game")
print("I am thinking of a number between 1 and 100 ")
level=input("choose the difficulty level easy or hard: ")
if level=="easy":
    guess(random.randint(1, 100),10)
elif level=="hard":
    guess(random.randint(1, 100),5)
else:
    print("please choose a valid level")

