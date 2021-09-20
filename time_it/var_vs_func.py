from timeit import timeit

def delimiter():
    print('-'*80)

def variable_tester(value):
    return timeit('tester()', setup=f'''
variable = {value}
def tester():
    return variable
    ''')

def function_tester(value):
    return timeit('tester()', setup=f'''
def function():
    return {value}
def tester():
    return function()
    ''')

def test_boolean_variable():
    return variable_tester(True)

def test_function_returns_boolean():
    return function_tester(True)

def test_int_variable():
    return variable_tester(1)

def test_function_returns_int():
    return function_tester(1)

def test_float_variable():
    return variable_tester(1.0)

def test_function_returns_float():
    return function_tester(1.0)

def test_string_variable():
    return variable_tester('"string"')

def test_function_returns_string():
    return function_tester('"string"')

def test_tuple_variable():
    return variable_tester((1, 2, 3))

def test_function_returns_tuple():
    return function_tester((1, 2 , 3))

def test_list_variable():
    return variable_tester([1, 2, 3])

def test_function_returns_list():
    return function_tester([1, 2, 3])

def test_set_variable():
    return variable_tester({1, 2, 3})

def test_function_returns_set():
    return function_tester({1, 2, 3})

def test_dictionary_variable():
    return variable_tester({'a': 1, 'b': 2, 'c': 3})

def test_function_returns_dictionary():
    return function_tester({'a': 1, 'b': 2, 'c': 3})

def main():
    delimiter()
    print(
        f'Calling Function that returns boolean runs in : {test_function_returns_boolean()} seconds')
    print(
        f'Calling boolean Variable runs in : {test_boolean_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns int runs in : {test_function_returns_int()} seconds')
    print(f'Calling int Variable runs in : {test_int_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns float runs in : {test_function_returns_float()} seconds')
    print(f'Calling float Variable runs in : {test_float_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns string runs in : {test_function_returns_string()} seconds')
    print(
        f'Calling string Variable runs in : {test_string_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns tuple runs in : {test_function_returns_tuple()} seconds')
    print(f'Calling tuple Variable runs in : {test_tuple_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns list runs in : {test_function_returns_list()} seconds')
    print(f'Calling list Variable runs in : {test_list_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns set runs in : {test_function_returns_set()} seconds')
    print(f'Calling set Variable runs in : {test_set_variable()} seconds')
    delimiter()
    print(
        f'Calling Function that returns dictionary runs in : {test_function_returns_dictionary()} seconds')
    print(
        f'Calling dictionary Variable runs in : {test_dictionary_variable()} seconds')
    delimiter()

if __name__ == '__main__':
    main()
