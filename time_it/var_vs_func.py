from timeit import timeit

def test_variables():
    return timeit('''
variable = 'value'
def tester():
    return variable
''')

def test_functions():
    return timeit('''
def function():
    return 'value'
def tester():
    return function()
''')

print(f'Calling Functions runs in : {test_function()} seconds')
print(f'Calling Variables runs in : {test_variable()} seconds')
