# Problem Day 4 (HARD)

# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
 
# You can modify the input array in-place.

from random import seed
from random import randint
from random import random

# O(N) and S(1)
def search_minimun_missing_positive_best_way(arr):

    # Lenght of array 
    maximun = len(arr)

    # First iteration. Worst case => O(n)
    for i in range(maximun):
        
        # If is negative or is greater than array size
        # it has no sense to process.
        # Move to next element
        if (arr[i] <= 0 or arr[i] >= maximun):
            continue
        

        val = arr[i]

        # Swap positions with numbers
        # to have concordance with the array position
        while (arr[val-1] != val):
            next_val = arr[val-1]
            arr[val-1] = val
            val = next_val

            # If is negative or is greater than array size
            # it has no sense to process.
            # Move to next element
            if ((val >= maximun) or (val <= 0)):
                break

    # Check for the element array which 
    # not matches with its position
    # Second iteration. Worst case => O(n)
    for i in range(maximun):
        if (arr[i] != i + 1):
            return i + 1
    
    # If the for above doesn't return anything
    # it means the next positive integer is missing
    return maximun + 1


# O(n) and Space (n)
def search_minimun_missing_positive_alternative_way(arr):

    posibilities = {}

    for i in arr:
        if ((i not in posibilities.keys()) and (i >= 0) and (i < len(arr))):
            posibilities[i] = 1

    for i in range(1, len(arr)):
        try:
            posibilities[i]
        except Exception:
            return i
    
    return len(arr)

if __name__ == "__main__":
    
    test_arrays = [ [2,2,1],
                    [3,4,-1,1],
                    [1,4,2,0],
                    [1,2,100],
                    [1,2,6,8,2,2,2,2,-14,100]
                ]

    for test in test_arrays:
        print("-------------------TEST FOR %s-----------------" % test)
        print("search_minimun_missing_positive_best_way \t\t=> %s" % search_minimun_missing_positive_best_way(test))
        print("search_minimun_missing_positive_alternative_way => %s" % search_minimun_missing_positive_alternative_way(test))
        print("-----------------------------------------------------" % test)

    # Doing some randoms integer...
    
    # seed random number generator
    seed(1)
    randon_arr = []

    # generate some integers
    for _ in range(512):
        mult = 1 if random() < 0.5 else -1
        randon_arr.append(mult * randint(-20, 35))

    print(randon_arr)
    print("Minimun positive integer missing search_minimun_missing_positive_best_way \t\t\t=> %s" %  search_minimun_missing_positive_best_way(randon_arr))
    print("Minimun positive integer missing search_minimun_missing_positive_alternative_way \t=> %s" % search_minimun_missing_positive_alternative_way(randon_arr))