'''
    Sample Input: [1, 3, 5, 2, 7, -3], targetSum = 6
    Sample Output: [1, 5]

    Sample Input: [1, 3, 5, 2, 7, -3], targetSum = 11
    Sample Output: [-1, -1]
'''

# Method 1: Check every pair using two loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Brute force Solution
def find_pair(arr, target_sum):

    for i in range(len(arr) - 1): # O(n)
        
        for j in range(i + 1, len(arr) ): # O(n)
        
            if arr[i] + arr[j] == target_sum:
                return [ arr[i], arr[j] ] 
    
    return []


# Method 2: Sort and check all the pairs until arr[i] + arr[j] < targetSum
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def find_pair_2(arr, target_sum):
    arr.sort() # O(n * log (n))

    for i in range(len(arr)-1): # O(n)
        
        for j in range(i+1, len(arr)): # O(n)
            current_sum = arr[i] + arr[j]
            
            if current_sum == target_sum:
                return [arr[i], arr[j]]
            elif current_sum > target_sum:
                break

    return []


# Method 3: Two pointer approach
# Time Complexity: O(n * log n)
# Space Complexity: O(1)
def find_pair_3(arr, target_sum):
    arr.sort() # O(n * log n)

    left, right = 0, len(arr)  - 1
    
    while left < right: # O(n)
        current_sum = arr[left]+arr[right]

        if current_sum == target_sum:
            return [arr[left], arr[right]]
        
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1 
    
    return []

# Method 4: Use extra space to keep track of keys available
# Time Complexity: O(n)
# Space Complexity: O(n)
def find_pair_4(arr, target_sum):
    arr_dict = {}
    
    # for i in arr: # O(n)
    #     arr_dict[i] = True
    
    for val in arr: # O(n)
        other_key = target_sum - val

        if arr_dict.get(other_key):
            return [val, other_key] 

        arr_dict[val] = True

    return []



arr = [-7, -5, -3, -1, 0, 1, 3, 5, 7]
target_sum = -5

result = find_pair_4(arr, target_sum)

print(result)
