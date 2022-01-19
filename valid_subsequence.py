'''
    Sample Input: 
        arr = [5, 1, 7, 16, 22, -5]
        subseq = [1, 16, -5]
    
    Sample Output: True

    
    Sample Input: 
        arr = [5, 1, 7, 16, 22, -5]
        subseq = [1, 5, 22]
    
    Sample Output: False
'''

# Time Complexity: O(n)
def is_valid_subsequence(array, subsequence):
    array_idx, subsequence_idx = 0, 0

    while array_idx < len(array) and subsequence_idx < len(subsequence): # O(N)
        if array[array_idx] == subsequence[subsequence_idx]:
            subsequence_idx += 1
        
        array_idx += 1

    return subsequence_idx == len(subsequence)
    

# Time Complexity: O(n)
def is_valid_subsequence_2(array, subsequence):
    subseq_index = 0
    for val in array:
        if subseq_index == len(subsequence):
            break
        if val == subsequence[subseq_index]:
            subseq_index += 1

    return subseq_index == len(subsequence)


arr = [5, 1, 7, 16, 22, -5]
#subseq = [1, 16, -5]
subseq = [1, 5, 22]


result = is_valid_subsequence_2(arr, subseq)
print(result)
