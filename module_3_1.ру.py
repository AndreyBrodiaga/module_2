calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()

    return  string.upper(), string.lower()


def is_contains(string, list_to_search):

    count_calls()

    return any(str_elem.lower() == string.lower() for str_elem in list_to_search)

string_info("Hello")
is_contains("world", ["World", "Python"])
string_info("Example")
is_contains("example", ["EXAMPLE", "TEST"])

print(string_info('Capibara'))
print(string_info('Armageddon'))
print('Urban',['ban','BaNaN','urBAN'])
print(is_contains('cycle',['recycling','cylic']))
print(f"{calls} ")
