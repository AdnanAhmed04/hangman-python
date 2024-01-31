import random
# guess = 'adnanahmed'

# guess = 'abcdefghijklmnopqrstuvwxyz'
guess=input('enter guess word : ')
print('the len of guess is', len(guess))

GUESS = guess
lower_limit = 0
upper_limit = len(guess) - 1

#random missing
random_element = random.choice(guess)
missing = ((len(guess) // 2) - 1)
print('total letters', missing, 'miss hogayee')

#random element missing
lst = []
random_integers = random.sample(range(lower_limit, upper_limit + 1), missing)
print(random_integers)

for i in range(len(random_integers)):
    lst.append(random_integers[i])

for j in lst:
    guess = guess[:j] + '-' + guess[j + 1:]

print(guess)
