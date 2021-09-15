# import time module
import time
import examples



begin = time.time()
print(examples.findprime(7,100000))
end = time.time()

print(begin , end )
result = end - begin
print(result)


