
import timeit


#insert ife into "testcode" to test variable speed
ife = "ife"


testcode= """
def f_ife():
    return "ife"
"""




result = timeit.timeit(stmt= testcode)

print(result)