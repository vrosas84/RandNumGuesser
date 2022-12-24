import random

name = input('Please enter your name: ')
range = input(f'Hello {name.capitalize()}, please type a number: ')

def isdigit(d):
    if d.isdigit():
        d = int(d)
        return d
    else:
        print('Please enter a number next time')
        quit()

def guesses(score):
    score = 0
    while True:
        guess = input(f'Enter a number between 0 and {str(range)}: ')
        guess = isdigit(guess)
        score += 1
        if guess == r:
            print(f'Congratulations {name.capitalize()}, you got it right!')
            return score
        elif guess > r:
            print('Too high')
            continue
        else:
            print('Too low')
            continue

range = isdigit(range)
r = random.randint(0, range)
score = guesses(r)
print('It took you', score, 'guesses')