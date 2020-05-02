import random
maxn = 10
n = random.randint(1, maxn)
print('Welcome!')
print('Guess the number between 1 and %d' % maxn)
guess = None
while guess != n:
    guess = int(input('Your guess: '))
    if guess > n:
        print('Too big')
    if guess < n:
        print('Too small')

print('You win!')
