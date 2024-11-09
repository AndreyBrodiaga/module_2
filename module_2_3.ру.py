my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_1 = []
i = 0

while i < len(my_list) and my_list[i] > 0:
    my_list_1.append(my_list[i])
    i += 1

print(my_list_1)