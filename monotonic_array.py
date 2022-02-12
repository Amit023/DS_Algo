'''
    WAF that takes an array of integers and 
    return a boolean representing  whether  the array is monotonic

    Non_Increasing => for index i < j, arr[j] <= arr[i]
    Ex: [-20, -25, -48, -48, -100]
    
    Non_Decreasing => for index i < j, arr[i] <= arr[j]
    Ex: [2, 8, 15, 32, 32, 45, 70]
'''

def isMonotonic(arr):
    isNonDecreasing, isNonIncreasing = True, True

    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            isNonDecreasing = False
        if arr[i-1] > arr[i]:
            isNonIncreasing = False
    
    return isNonIncreasing or isNonDecreasing

print(isMonotonic( [-20, -25, -48, -48, -100]))
print(isMonotonic( [2, 8, 15, 32, 32, 45, 70]))
print(isMonotonic( [2, 8, 7, 15, 32, 32, 45, 70]))