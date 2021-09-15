def findprime(x,y):
    list= []
    for z in range(x,y):
        if z > 1:
            # check for factors
            for i in range(2, z):
                if (z % i) == 0:
                    #print(z, "is not a prime number")
                    #print(i, "times", z // i, "is", z)
                    break
            else:
                list.append(z)
                #print(z, "is a prime number")

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            continue
            #print(z, "is not a prime number")

    return list






# transversal calculated manually
def max_transversal_(h):
    num = 1
    for x in range(h):
        num = num*2
    return num - 1




def max_transversal(h):
    num = ((2**h)-1)
    return num


height = 4
print(max_transversal(height))
print(max_transversal_(height))