'''
    Sample Input: [12, 3, 1, 2, -6, 5, -8, 6], targetSum = 0
    Sample Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''

# Brute Force: check every triplet
# Time Complexity O(n^3)
def three_number_sum(arr, target_sum):
    result = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target_sum:
                    result.append([ arr[i], arr[j], arr[k] ])
    result.sort()
    return result


# Use two pointer approach with key
def three_number_sum_2(arr, target_sum):
    res = []

    arr.sort() # O(N)
    
    for i in range( len(arr) - 2 ): # O(N)
        left, right = i+1, len(arr)-1

        while left < right: # O(N)
            sum = arr[left] + arr[right] + arr[i]
            if sum == target_sum:
                res.append( [ arr[i], arr[left], arr[right] ] )
                # print([ arr[i], arr[left], arr[right] ])
                # print("res: ",res)
                left += 1
                right -= 1

            elif sum < target_sum:
                left += 1
            else:
                right -= 1
    
    #res.sort()
    return res


arr = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print( three_number_sum_2(arr, targetSum) )