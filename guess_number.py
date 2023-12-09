import random
number = random.randint(1,1000)
attempts = 0
low = 1
high = 1000
while True:
    print('Guess the number (between 1 and 10000): ')
    input_number = (low+high)//2
    print('my guess is ',input_number)
    attempts+=1

    if input_number == number:
        print('yes , you are right')
        break
    if input_number >number:
        print('incorrect! please try again: ')
        high = input_number-1
    else:
        print('incorrect! please try again ')
        low = input_number+1
print('you tried,',prattempts,'times to find the correct number. ')