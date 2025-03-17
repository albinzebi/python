def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

number_inserted = input('Insert a number: ')
number_inserted = int(number_inserted)

if number_inserted >= 0:
    countdown(number_inserted)
else:
    countup(number_inserted)