'''
COEN 379 Winter 2021 Homework 3 Problem 3
Shiva Govindaraju
Using Python 3 to run simulation to complete homework-problem.
--Write a program to
---generate a set S of N = 100 random nonnegative integers less than P = 1000003 (a prime); and then
---generate for set S a random perfect universal hash function h(x) = ((ax + b) mod P)mod N^2, where 0 < a < P  and  0 ≤ b < P.
--How many tries did it take on average?
SOLUTION:
- On one attempt where I ran 100 simulations, the average number of tries was 1.73
- On another attempt w/ 100 sims, it was 1.7
- On a third attempt w/ 100 sims, it was 1.59
- When attempting w/ 50 sims, it was 1.84
- When attempting w/ 25 sims, it was 1.48
- When attempting w/ 10 sims, it was 1.5
- When attempting w/ 1000 sims, it was 1.616
'''
import random as rand

def gen_rand_S(N, P):
    rand.seed() # we seed the random number generator before making a new Set S
    rand_S = [-1] * N # initializing
    for i in range(N):
        rand_S[i] = rand.randrange(0, P) # non-negative numbers between 0 and P.
    if len(set(rand_S)) != len(rand_S): # must ensure that Set contains only unique elements
        rand_S = gen_rand_S(N, P) # if Set had non-unique elements, generate a new Set.
    return rand_S

def h_x(N, P, a, b, x):
    return (((a * x) + b) % P) % (N * N) # the hash-function described in the problem text.

def confirm_perfect_hash(N, P, S, a, b):
    table = [False] * (N * N) # vector containing flags to detect collisions in a hash-table.
    for x in S:
        key_hash = h_x(N, P, a, b, x) #first find the hash for a given key x
        if table[key_hash]: # if another value has already been assigned that key, a collision occured
            return False
        table[key_hash] = True # flag the key as in-use by key x
    return True # if no collisions were detected, it's a perfect hash function

def find_perfect_hash(N, P, S):
    found = False # initially haven't found the perfect hash function.
    a, b, tries = -1, -1, 0
    while not found: # we continue trying until we find a perfect hash function
        tries = tries + 1
        a = rand.randrange(1, P) # a and b are randomly selected in the ranges described in the problem
        b = rand.randrange(0, P)
        print("Try {} - a: {} b: {}".format(tries, a, b))
        if confirm_perfect_hash(N, P, S, a, b):
            found = True
    return a, b, tries # we return the a & b chosen for the perfect hash & the number of tries we took

if __name__ == "__main__":
    print("--- COEN 379 Winter 2021 Homework 3 Problem 3---")
    print("Preset values: N = 100. P = 1000003.")
    print("-----")
    sim_num = int(input("Please enter # of sims to run for avg. calcs.: "))
    try_sum = 0
    for sim in range(sim_num):
        # We'll generate a new random Set and a perfect hash function for it each simulation
        print("Simulation {}".format(sim + 1))
        S_sim = gen_rand_S(100, 1000003) # generate the random set S
        print("Random Set S: {}\n".format(S_sim))
        a_sim, b_sim, try_sim = find_perfect_hash(100, 1000003, S_sim) # find the a, b for perfect hash
        print("Found Perfect Hash!\nA : {} B: {} Tries: {}\n".format(a_sim, b_sim, try_sim))
        try_sum = try_sum + try_sim # running sum of tries to find perfect hashes
    print("-----\n\nAverage tries to find perfect hash: {}\n".format(try_sum / sim_num))
        
    
    