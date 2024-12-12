
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    total = 0

    for arg in args:
        if isinstance(arg, int):
            total += arg

        elif isinstance(arg, str):

            total += len(arg)

        elif isinstance(arg, dict):

            for key in arg.keys():
                total += calculate_structure_sum(key)
            for value in arg.values():
                total += calculate_structure_sum(value)

        elif isinstance(arg, (list, tuple, set)):

            for item in arg:
                total += calculate_structure_sum(item)

        else:
            pass

    return total




result = calculate_structure_sum(data_structure)
print(result)

