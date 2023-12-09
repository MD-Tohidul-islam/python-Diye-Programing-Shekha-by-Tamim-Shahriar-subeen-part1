import string
string1 = 'Hello Test! 123 123, good.'
capital = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
other = string.punctuation
sr1 = ''
sr2 = ''
sr3 = ''
sr4 = ''
for i in string1:
    if i in capital:
        sr1+=i
    elif i in lower:
        sr2+=i
    elif i in number:
        sr3+=i
    elif i in other:
        sr4+=i
print(sr1)
print(sr2)
print(sr3)
print(sr4)

