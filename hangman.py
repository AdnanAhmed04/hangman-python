import random
guess=input('enter guess word : ')
# print('the len of guess is', len(guess))

GUESS = guess
lower_limit = 0
upper_limit = len(guess) - 1

#random missing
random_element = random.choice(guess)
missing = ((len(guess) // 2) - 1)
# print('total letters', missing, 'miss hogayee')
# if missing<=4:
#     print('too short and it is too easy')

#random element missing
lst = []
random_integers = random.sample(range(lower_limit, upper_limit + 1), missing)

for i in range(len(random_integers)):
    lst.append(random_integers[i])

for j in lst:
    guess = guess[:j] + '-' + guess[j + 1:]

print(guess)

count=missing
element=[]
for j in GUESS:
    element.append(j)
print(element)

missing_element=[]
for k in guess:
    missing_element.append(k)
print('missing element',missing_element)

for j in range(1,missing*2):
#     print(j,missing)
    missing=missing-1
    letter=input('enter a missing letter : ')
    index=int(input('enter where u want to add letter : '))
    if letter[index] in element:
        
print(missing_element)
    
