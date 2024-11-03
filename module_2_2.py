first = int(input('введите число: '))
print('first')
second = int(input('введите число: '))
print('second')
third = int(input('введите число: '))
print('third')
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')

