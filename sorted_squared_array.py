'''
    Sample Input: 
        arr = [1, 3, 4, 5, 7]
        
    Sample Output:  [1, 9, 16, 25, 49]
    
    Sample Input: 
        arr = [-5, -3, -1, 2, 4, 6]
    
    Sample Output: [1, 4, 9, 16, 25, 36]
'''
# Square and Sort
# Complexity: O(n*logn) | Space Complexity: O(1)
def sorted_squared_array(arr):
    arr = [arr[i] * arr[i] for i in range(len(arr))]
    arr.sort()
    
    print(arr)


# Square and Two pointer approach to pick element in sorted way
# Complexity: O(n*logn) | Space Complexity: O(1) 
def sorted_squared_array_2(arr):
    arr = [arr[i] * arr[i] for i in range(len(arr))] # O(n)

    output = [0] * len(arr)
    i, j = 0, len(arr) - 1

    idx = len(arr) - 1

    while i <= j: # O(n)
        
        if arr[i] < arr[j]:
            output[idx] = arr[j]
            j -= 1
        else:
            output[idx] = arr[i]
            i += 1
        
        idx -= 1
    
    print(output)
        

arr1 = [1, 3, 4, 5, 7]
arr2 = [-5, -3, -1, 2, 4, 6]
sorted_squared_array_2(arr2)