# for i in range(10):
#     print("i is now {}".format(i))


# i = 0
#
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# exits = ["north", "east", "south"]
#
# chosen_exit = ''
# while chosen_exit not in exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("You got out")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it the first time")

