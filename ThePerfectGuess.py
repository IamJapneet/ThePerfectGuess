#This code was written by Japneet on 3rd March 2022, Thank you for reading!


import random
randomnumber=random.randint(1,100)
userguess=None
guesses=0
while userguess!=randomnumber:
    userguess=int(input("Enter your guess\n"))
    guesses=guesses+1
    if userguess==randomnumber:
        print("Congrats🎉, You guessed it right!")
    else:
        if userguess>randomnumber:
            print("You guessed a wrong number😬! Enter a smaller number")
        else:
            print("You guessed a wrong number😬! Enter a larger number")
print (f"you guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    highscore=int(f.read())

if guesses<highscore:
    print("You just broke the high score!, Congrats🥳")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))


