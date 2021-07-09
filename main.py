import random
randnumber = random.randint(1,100)
# print(randnumber)

userguess = None
guesses = 0

while(userguess != randnumber):
    userguess = int(input("Enter your guess: "))
    guesses += 1

    if (userguess==randnumber):
        print("You Guessed it right!")
    else:
        if(userguess>randnumber):
            print("You Guessed it wrong! Enter a small number")
        else:
            print("You Guessed it wrong! Enter a large number")
    
print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
with open("hiscore.txt","w") as f:
    f.write(str(guesses))