import timeit
import Bruteforce_new


setup = """
import Bruteforce
"""
#testcode= """


#Bruteforce.main(False)

#"""

# Because we are passing in an input we change number to one to only run once
#result = timeit.timeit(setup=setup, stmt=testcode, number=1)


# print(result)
# print("there is a difference in numbers because timit is accounting for the time taken to push password input")


setup = """
import Bruteforce_new
"""


testcode = """
Bruteforce_new.main(False,"ife")

"""
setup1= """
import bruteforce_as_class
"""


testcode1= """
crack = bruteforce_as_class.main("ife",False)
crack.test()

"""
result = timeit.timeit(setup=setup, stmt=testcode, number=1)
print(result)

result = timeit.timeit(setup=setup1, stmt=testcode1, number=1)
print(result)