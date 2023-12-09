teminate = False
while not teminate:
    n1 = int(input('please enter a number: '))
    n2 = int(input('please enter another number: '))
    while True:
        operation = input('please enter add/sub or quit to exit: ')
        if operation == "quit":
            teminate = True
            break
        if operation not in ['add','sub']:
            print('unknown operation')
            continue
        if operation == 'add':
            print('Result is :' ,n1+n1)
            break
        if operation == 'sub':
            print('result is ', n1-n2)
            break
