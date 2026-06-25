import random

num = random.randint(1, 10)

tries = 0

while True:
    guess = int(input("Guess your number between 1 - 10: "));
    
    print(num)

    if guess == num:
        tries += 1
        print(f"you are right, you guess the number in {tries} tries")
        break
        
    elif num < guess:
        tries += 1
        print("go a little lower")
        
    elif num > guess:
        tries += 1
        print("go a litle higher")
        
    else:
        tries += 1
        print("you are wrong")