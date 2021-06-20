'''
COEN 379 Winter 2021 Homework 1 Problem 3
Shiva Govindaraju
Using Python 3 to run simulation to complete homework-problem.
--Write a linear-time function to shuffle an array of n elements so that any permutation appears as the outcome with probability LaTeX: \frac{1 }{ n!}1 n !.
'''
import random as rand

'''
*Essentially, we start from the start of the array (index 0) and pick an element from the remainder of the array (from 1 to n-1) and swap the two elements. Then, we keep the new 0th element as fixed and move onto swapping for a new 1-th element, then for a 2-nd element, then a 3-rd. When we get to picking index n-2, the only one left to swap with is n-1, so we stop rather than have n-1 swap with itself constantly.
*The randomness of what we pick to swap ensures that the permutation is random and the probability of any given permutation is 1/(n!).
*This function is linear: there is a single loop with n-1 iterations (ie, O(n)) and the inside of the loop operates in O(1) time. Therefore, the entire function is O(n) and thus linear.
'''
def linear_shuffle(arr, n):
    '''
    Will shuffle the array in-place. Assumes array contains distinct, unique values.
        arr: an array of integers
        n:   size of arr
    '''
    for index in range(n - 1): # increment from 0 to n-2
        rand_ind = rand.randint(index, n - 1) # find an index to swap with in [index, n)
        arr[index], arr[rand_ind] = arr[rand_ind], arr[index] # swap arr[ind] and arr[rand-ind] to shuffle
    return arr

if __name__ == "__main__":
    print("--- COEN 379 Winter 2021 Homework 1 Problem 3---")
    n = int(input("Enter value for n: "))
    test_arr = list(range(0, n))
    print("Starting Array: {}\n".format(test_arr))
    new_arr = linear_shuffle(test_arr, n)
    print("Shuffled Array: {}\n".format(new_arr))