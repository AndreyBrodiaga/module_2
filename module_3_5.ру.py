
def get_multiplied_digits(number):
    str_number = str(abs(number))

    if not str_number or set(str_number) == {'0'}:
        return 0

    first = int(str_number[0])

    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(123450)
print(result2)

