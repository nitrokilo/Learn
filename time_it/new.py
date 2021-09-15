import timeit

setup = """
import Bruteforce_new
"""

testcode = """
Bruteforce_new.main(True,"ife")

"""

result = timeit.timeit(setup=setup, stmt=testcode, number=1)
print(result)

