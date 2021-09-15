print("Learning to use timeit")

# Import Timeit
import timeit

#print numbers between 0 - 1000




targetcode = """
x=700 
y = x + 2 -100 + 100 
"""


result = timeit.timeit(stmt=targetcode)
print(result)


