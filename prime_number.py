def is_prime(n):
    if n<2:
        return False
    prime = True
    for i in range(2,n):
        if n%i==0:
            print(n,'is devisible by',i)
            prime = False
    return prime


while True:
    number = int(input('enter a number : '))
    if number == 0:
        break
    prime = is_prime(number)
    if prime is True:
        print(number,'is a prime number.')
    else:
        print(number,'is not a prime number.')