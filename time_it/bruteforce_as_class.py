# Inspired by
# https://github.com/CyanCoding/Brute-Force-Password-Cracker/blob/master/Python/main.py
# Bruteforce calculation as a class


# import Statements
import itertools
import time


class main():
    def __init__(self,password,show):
        self.password = password
        self.show = show


    #pre-resequite functions
    def tryPassword(self,passwordSet, stringTypeSet,show):
        start = time.time()
        chars = stringTypeSet
        attempts = 0
        for i in range(1, 9):
            for letter in itertools.product(chars, repeat=i):
                attempts += 1
                letter = ''.join(letter)
                if show:
                    print(letter)
                if letter == passwordSet:
                    end = time.time()
                    distance = end - start
                    return (attempts, distance)
    # Password find method
    def test(self):
        password = self.password
        # Allowed characters
        stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
        tries, timeAmount = self.tryPassword(password, stringType, self.show)
        print("CyanCoding's BFPC cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))


