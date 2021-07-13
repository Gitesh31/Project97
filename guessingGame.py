import random
import math

lower = int(input("Enter Lower bound:- ")) 
upper = int(input("Enter Upper bound:- "))

g = random.randint(lower, upper)

print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the Number\n")
 
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))
 
    if g == guess:
        print("Congratulations you have guessed Correct! ",
              count, " try")
        break
    elif g > guess:
        print("You Guess is too Small")
    elif g < guess:
        print("You Guess is too Big")
 
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is ",g)
    print("\tBetter Luck Next time!")