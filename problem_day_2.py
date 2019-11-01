# Problem day 2 (HARD)
# Given an array of integers, return a new array such that each element at index i of the new array is the 
# product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def array_product_process(arr):

    response = [1] * len(arr) 
    for i in range(len(arr)): 
        for j in range(len(arr)):
            if i != j:
                response[i] *= arr[j]
        
    return response

def array_product_process_with_division(arr):

    total = 1
    for i in arr:
        total *= i
    
    response = [total] * len(arr)
    for i in range(len(arr)):
        response[i] /= arr[i]
    
    return response

def array_product_process_without_division(arr):

    response = [1] * len(arr)

    left = [1] * len(arr)
    right = [1] * len(arr)
    
    for i in reversed(range(0, len(arr)-1)):
        right[i] = right[i+1] * arr[i+1]  
    
    for i in range(1,len(arr)):
        left[i] = left[i-1] * arr[i-1]    
    
    for i in range(len(arr)):
        response[i] = right[i] * left[i]
    
    return response


print(array_product_process([1, 2, 3, 4, 5]))
print(array_product_process([3, 2, 1]))

print(array_product_process_with_division([1, 2, 3, 4, 5]))
print(array_product_process_with_division([3, 2, 1]))

print(array_product_process_without_division([1, 2, 3, 4, 5]))
print(array_product_process_without_division([3, 2, 1]))
