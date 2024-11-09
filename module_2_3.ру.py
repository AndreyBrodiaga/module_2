my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_1 = []

for number in my_list:
    if number <= 0:
        break
    my_list_1.append(number)

print(my_list_1)