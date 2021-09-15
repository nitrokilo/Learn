# original code taken from github
# https://github.com/CyanCoding/Brute-Force-Password-Cracker/blob/master/Python/main.py

# Imports
import itertools
import time


# Brute force function
def tryPassword(passwordSet, stringTypeSet, show):
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

def main(show,key):
    password = key
    # Allowed characters
    stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    tries, timeAmount = tryPassword(password, stringType, show)
    print("CyanCoding's BFPC cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))
