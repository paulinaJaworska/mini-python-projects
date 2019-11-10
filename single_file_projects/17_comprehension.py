''' Program tells user to guess random number between 1 and 20 in 6 guesses'''
import random  #import the random module's fuctionalities

guesses_taken = 0  # set number of guesses taken to zero

print('Hello! What is your name?')  # ask for the player's name
myName = input()  # take an input from the player and and assign it to myName variable

number = random.randint(1, 20)   # select a random number between 1 and 20 and assign it to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # display message initiating game 

while guesses_taken < 6:  # set max. number of attempts to six
    print('Take a guess.')  # ask the player for his guess
    guess = input()  # take player's input and assign it to guess variable
    guess = int(guess)  # convert player's guess to intiger

    guesses_taken += 1  # increase number of attempts after the guess

    if guess < number:  # check if player's guess is smaller than the number to guess
        print('Your guess is too low.')  # display that guess is too low

    if guess > number:  # check if player's guess is higher than the number to guess
        print('Your guess is too high.')  # display that guess is to high

    if guess == number:  # check if player's guess is equal the number to guess
        break  # break the loop of attempts

if guess == number:  #  check if player's guess is equal the number to guess
    guesses_taken = str(guesses_taken)  # convert current number of attempts to string data type
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  # display the winning message.

if guess != number: # check if player's guess after possible number of attempt is not the same as number to guess
    number = str(number)  # convert number to guess to string data type
    print('Nope. The number I was thinking of was ' + number)  # display the messange with the number that was't guessed by player
