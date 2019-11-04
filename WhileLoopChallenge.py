import random

answer = random.randint(1, 10)

print("Please enter a value from 1 - 10: ")
guess = 0

while guess != answer:
    guess = int(input())
    if guess == answer and guess != 0:
        print("Well done")
    else:
        if guess == 0:
            print("Come play again bye bye")
            break
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        print("Try again")


