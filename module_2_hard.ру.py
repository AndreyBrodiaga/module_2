def find_pairs(target_sum, range_limit):
    pairs = set()

    for a in range(1, range_limit + 1):
        for b in range(1, range_limit + 1):
            total = a + b
            
            if total == target_sum:
                
                pairs.add((min(a, b), max(a, b)))

    return pairs



target_sum = int(input('введите число от 3 до 20: '))
range_limit = 20


result_pairs = find_pairs(target_sum, range_limit)


result_string = ''.join(f"{a}{b}" for a, b in result_pairs)


print(result_string)
