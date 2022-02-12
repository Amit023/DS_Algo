'''
    Given an integer array and an integer
    Move the integer at the end of the array

    Sample Input: [2, 1, 2, 2, 2, 3, 4, 2], 2
    Sample Output: [1, 3, 4, 2, 2, 2, 2, 2, 2]
'''

# Time Complexity: O(N), Space Complexity: O(1)
def move_element_to_end(arr, n):
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] == n:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    
    return arr

print( move_element_to_end([1, 3, 4, 2, 2, 2, 2, 2, 2], 2) )