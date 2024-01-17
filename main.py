#!/usr/bin/env python3
import random
import math

#Taking inputs
lower = int(input("Enter a lower bound:- "))

#Taking inputs
upper = int(input("Enter a upper bound:- "))

#Generate a random number between the upper and lower
X = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1,2)), " chances to guess the integer!\n")

#initalizing count
count = 0
# for calculation of minimum number of
# guesses depends upon rang
while count < math.log(upper - lower):
    count += 1

guess = int(input("Guess a number:- "))

if X == guess:
    print("congrats you did it in", count, "try")
#Once guessed the loop end
    break
#Testing condition
elif X > guess:
    print("you guess too high!")
elif X < guess:
    print("you guess too low!")
#If guessing more than the required guess
#Show this output
while count > math.log(upper - lower):
    print("\n The number is %d" % X)
    print("\tBetter Luck Next time!")

