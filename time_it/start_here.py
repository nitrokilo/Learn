print("Learning to use timeit")

# Import Timeit
import timeit




targetcode = """

def test(num):
    for x in range(num):
        y = num ** 4
        y = y - (y * .000001)
        return y 

test(10000000000000000000)

"""


result = timeit.timeit(stmt=targetcode)
print(result)