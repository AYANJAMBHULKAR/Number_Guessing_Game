import random


def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2

        # If guess is in the middle, It is found!

        if guess == randnum:
            return count

        # If "guess" is greater than the number,
        # It must be found in the lower half of the set of numbers
        # Between the lower value and the guess.

        elif guess > randnum:
            count = count + 1
            return computerGuess(lowval, guess - 1, randnum, count)

        # The number must be in the upper set of numbers
        # Between the guess and the upper value

        else:
            count = count + 1
            return computerGuess(guess + 1, highval, randnum, count)

    else:

        # Number not found

        return -1


# End of Function


# Generate a random number between 1 and 100

randnum = random.randint(1, 101)

count = 0
guess = -99

while (guess != randnum):
    # Get the user's guess

    guess = (int)(input('Enter your guess between 1 and 100: '))

    if guess < randnum:
        print('Higher')

    elif guess > randnum:
        print('Lower')

    else:
        print('You Guessed it! \n')
        break

    count = count + 1

# End of While Loop

print('You took ' + str(count) + ' steps to guess the number \n')

print('Computer took ' + str(computerGuess(1, 100, randnum)) + ' steps! \n')