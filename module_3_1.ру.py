
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()

    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):

    count_calls()

    return any(str_elem.lower() == string.lower() for str_elem in list_to_search)

string_info("Hello")
is_contains("world", ["World", "Python"])
string_info("Example")
is_contains("example", ["EXAMPLE", "TEST"])


print(f"Всего было {calls} вызова.")
