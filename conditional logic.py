my_many = 30
rickshaw_fare = 40
if my_many >= rickshaw_fare:
    print('you can run on rickshaw!')
today = 'friday'

# if
saare = ['afghanistan', 'bangladesh', 'india', 'pakistan', 'nepal', 'bhutan', 'srilanka']
country = input('enter your country name: ')
if country in saare:
    print(country, 'is member of saare')
else:
    print(country,'is nor member of saare!!😞')
print('programe terminated')

# # grade calculator
marks = int(input('enter your marks: '))
if marks>=80:
    grade = 'A+'
elif marks>=70:
    grade = 'A'
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "F"
print('YOUR grade is: ',grade)
# # check +-
number = int(input('enter a number: '))
if number<0:
    print(number, 'is negative')
else:
    print(number, ' is positive')
# # even odd check
number1 = int(input('enter a number: '))
if number1%2==0:
    print(number1 , 'is even')
else:
    print(number1, 'is odd')