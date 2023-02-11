#guessing game
import random as r
secret_number = r.randint(1,10)
guess_count=1
while guess_count <= 3:
    userinput = int(input("I am thinking of a number 1 through 10 can you guess what it is?"))
    if userinput == secret_number:
        print("Well done you were able to get my number in",guess_count,"Guesses")
        break        
    else:
        print("Wrong! Guesses left:",3-guess_count)
        guess_count = guess_count + 1
if guess_count == 4:
    print("You failed! Better luck next time! The correct number was",secret_number,)
