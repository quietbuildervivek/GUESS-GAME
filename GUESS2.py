import random

comp=random.randint(1, 100)
guess=int(input("Guess the number :"))
count=0
for i in range(1,100):
    count += 1
    if guess==comp:
        print("gussed RIGHT")
        print(f"It took you {count} guesses.")
        break
    elif guess>comp:
        print("gussed HIGH")
        guess=int(input("Guess the number :"))
    else:
        print("gussed LOW")
        guess=int(input("Guess the number :"))
    