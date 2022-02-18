'''
    WAP to return the first duplicate value when iterating from left to right else return -1
    (Given an array integers are between 1 and n)

    Sample Input: [2, 1, 5, 2, 3, 3, 4]
    Sample Output: 2  
'''

# Time Complexity: O(n^2)
def first_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

    return -1

# Time Complexity: O(n) Space Complexity: O(1)
def first_duplicate_2(arr):
    s = set()

    for i in arr:
        if i in s:
            return i
        else:
            s.add(i)
    return -1

# Time Complexity: O(n)
def first_duplicate_3(arr):
    for i in arr:
        absValue = abs(i)
        if arr[ absValue - 1 ] < 0:
            return absValue
        arr[absValue - 1] *= -1
    return -1


print( first_duplicate_2( [2, 1, 3, 2, 5, 3, 4]) )
