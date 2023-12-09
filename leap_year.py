year = int(input('enter a year: '))
if year%4 == 0:
    if year% 100 == 0:
        if year % 400 ==0:
            print(year,'is leap year' )
        else:
            print(year,'is not  leap year' )
    else:
        print(year,'is leap year')
else:
    print(year,'is  not leap year')
## other
if year % 100 !=0 and year %4 == 0:
    print(year,'is leap year')
elif year %100 == 0 and year % 400 ==0:
    print(year,'is leap year')
else:
    print(year,'is not leap year')
