def find_pairs(target_sum, range_limit):
    pairs = set()  # Используем множество для уникальности пар

    # Проходим по всем возможным парам (a, b)
    for a in range(1, range_limit + 1):
        for b in range(1, range_limit + 1):
            total = a + b
            # Проверяем, равна ли сумма целевому значению
            if total == target_sum:
                # Добавляем пару в множество (в виде кортежа)
                pairs.add((min(a, b), max(a, b)))  # Сохраняем пары в отсортированном порядке

    return pairs  # Возвращаем множество пар


# Задаем целевую сумму и предел диапазона
target_sum = int(input('введите число от 3 до 20: '))
range_limit = 20

# Находим пары
result_pairs = find_pairs(target_sum, range_limit)

# Формируем сплошной цифровой ряд
result_string = ''.join(f"{a}{b}" for a, b in result_pairs)

# Выводим результат
print(f"ваш код :")
print(result_string)
