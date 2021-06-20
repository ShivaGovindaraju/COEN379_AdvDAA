'''
COEN 379 Winter 2021 Homework 2 Problem 2
Shiva Govindaraju
Using Python 3 to run simulation to complete homework-problem.
--Write a program to find the first 20 Carmichael numbers.
SOLUTION:
[561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401]
'''
from math import sqrt
from math import gcd # The Python3 math library's implementation of gcd
                     # is faster than the Instructor's C++ code.
                     # Similarly, we will use Python3's built-in pow() function for power-mod

def is_carmichael(n):
    if (n % 2 == 0): # if n is even, it's never going to be a Carmichael number
        return False
    factor_found = False
    s = sqrt(n)
    for a in range(2, n):
        if ((a > s) and not factor_found):
            # If a factor cannot be found in a < sqrt(n), n isn't likely a Carmichael number.
            return False
        if (gcd(a, n) > 1):
            # A factor > 1 has been found using a, meaning n is definitely not-prime.
            factor_found = True
        elif (pow(a, n-1, n) != 1):
            # The GCD of a and n is 1. If Fermat's test returns non-Prime, it's not a Carmichael number.
            return False
    # Haven't been able to prove it's prime or a non-Carmichael
    # So it much be a Carmichael
    return True

if __name__ == "__main__":
    print("--- COEN 379 Winter 2021 Homework 2 Problem 2---")
    carm_num = int(input("How many Carmichael Numbers should I find?: "))
    is_carm = [0] * carm_num
    found = 0
    test = 560 # we know the smallest Carmichael number is 561.
    while found < carm_num:
        if is_carmichael(test):
            is_carm[found] = test
            found = found + 1
        test = test + 1
    print("Found: {}\nFirst {} Carmichael Numbers: {}".format(found, carm_num, is_carm))
    