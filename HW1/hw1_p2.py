'''
COEN 379 Winter 2021 Homework 1 Problem 2
Shiva Govindaraju
Using Python 3 to run simulation to complete homework-problem.
--Let C_k be the number of unique array elements visited by rfind() in k iterations of the while loop. Find a closed-formed formula for E[C_k].  Does your formula agree with experimental data ?
'''
import random as rand

'''
*Here, we're going to just attempt experimental data for the second question, in order to confirm the formula.
'''
def rfind(vector, n, target):
    '''
    Adapting rfind() from lecture notes to Python3
    Added modifications to provide experimental data for checking Problem 2 answer.
        vector: an array of integers (assuming distinct integers)
        n: length of vector
        target: the value to be found
    '''
    visited = [False] * n
    count = 0
    k = 0 # added to keep track of iterations
    while (count < n):
        k = k + 1 # iteration tracker
        i = rand.randint(0, n-1)
        if not visited[i]:
            visited[i] = True
            count = count + 1
            if vector[i] == target:
                return i, count, k
    return -1, count, k

if __name__ == "__main__":
    print("--- COEN 379 Winter 2021 Homework 1 Problem 3---")
    n = int(input("Enter value for n: "))
    test_arr = list(range(0, n))
    rand.shuffle(test_arr)
    print("Starting Array: {}\n".format(test_arr))
    target = int(input("Enter target value: "))
    found, count, k = rfind(test_arr, n, target)
    if found >= 0:
        print("Found target value! Index: {}\n".format(found))
    else:
        print("Failed to find target value.\n")
    print("Unique Count: {} -- K: {}\n".format(count, k))
    
    # From here, I will be attempting to confirm my closed-form formula for E[C_k]
    run_num = int(input("Attempting multiple runs...\nEnter a number of simulation trials: "))
    unique_cnt = [-1] * run_num
    k_val = [-1] * run_num
    expect = [-1] * run_num
    for run in range(run_num):
        _, unique_cnt[run], k_val[run] = rfind(test_arr, n, target) # the actual experimental data.
        # the Closed-Form Formula I came up with.
        # rather then interrupt at the end of it, I just checked at the end of the rfind() function
        # once the data had been fully found. This made coding a little easier.
        expect[run] = n * (1 - ((n - 1 ) / n) ** k_val[run])
    print("Results:\nUnique: {}\nK-Vals: {}\nExpect: {}\n".format(unique_cnt, k_val, expect)) #for display
    for i in range(run_num):
        expect[i] = unique_cnt[i] - expect[i]
    print("Actual - Expect: {}\n".format(expect)) # just to confirm margin of error.