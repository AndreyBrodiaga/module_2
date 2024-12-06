def product_of_digits(number):
    number_str = str(number)
    
    non_zero_digits = [int(digit) for digit in number_str if digit != '0']
    
    if not non_zero_digits:
        return 0

    result = 1
    for digit in non_zero_digits:
        result *= digit
        
    return result



result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(123450)
print(result2)

