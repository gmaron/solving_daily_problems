# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# This is TC = O(n) and SC = O(n)
def calculate_sum(arr):

    prevOne, prevTwo, res = 0, 0, 0

    for i in range(len(arr)):
        if i == 0:
            res = arr[0]
        if i == 1:
            res = max(arr[0], arr[1])
        else:
            res = max(prevOne, arr[i] + prevTwo)

        prevTwo = prevOne
        prevOne = res

        # print("nIncl", prevOne)
        # print("nExcl", prevTwo)
    
    return res


test1 = [2, 4, 6, 2, 5]
test2 = [5, 1, 1, 5]
test3 = [-1, 0, 0, 1]

print("Testing...")
assert (calculate_sum(test1)) == 13
assert (calculate_sum(test2)) == 10
assert (calculate_sum(test3)) == 1
