print("Learning to use timeit")

# Import Timeit
import timeit






targetcode = """
x=700 
y = x + 2 -100 + 100 
"""


result = timeit.timeit(stmt=targetcode)
print(result)


