# Template for comparison
import timeit
import examples

setup = """

import max_transversal
"""


testcode = """ """


testcode1 =""" """


result1= timeit.timeit(stmt=testcode, setup=setup)
result2 = timeit.timeit(stmt=testcode1, setup=setup)


print(result1,result2)
