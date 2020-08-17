import random

colors = ['red', 'blue', 'orange', 'yellow', 'white', 'grey', 'black']

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking a color, can you guess that color")

    while True:
        if(color.lower() == guess.lower()):
            break
        else:
            guess = input("Nope. try again")

    print("You guessed it I was thinking about",color)

    play_again = input("Let's play again? Type 'no' to quit")

    if(play_again.lower() == 'no'):
        break
     
    
