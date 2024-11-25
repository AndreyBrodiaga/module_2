def generate_password(n):
    result = ''
    a = 1
    while a <= 20:
        b = a + 1
        while b <= 20:
            if n % (a + b) == 0:
                result += str(a) + str(b)
            b += 1
        a += 1

    return f'{n}-{result}'

n = 3
while n <= 20:
    print(generate_password(n))
    n += 1


