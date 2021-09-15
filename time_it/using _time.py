# import time module
import time







def test(num):
    for x in range(num):
        y = num ** 4
        y = y - (y * .000001)
        return y


begin = time.time()
test(10000000000000000000)
end = time.time()

print(begin , end )
#result = begin - end
#print(result)


