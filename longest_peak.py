'''
    WAP to find the longest peak
    peak is defined as adjacent elements in the array which are first strictly increasing and then
    strictly decreasing
    Sample Input: [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    Sample Output: 6 # 0, 10, 6, 5, -1, -3  
'''
from gettext import lngettext


def longest_peak(arr):
    if len(arr) < 3:
        return 0

    longest_peak = 0
    
    i = 1
    while i < len(arr) - 1:
        
        isPeak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
        if not isPeak:
            i += 1
            continue
            
        left = i - 1
        while left > 0 and arr[left] > arr[left - 1]:
            left -= 1
        
        right = i + 1
        while right < len(arr) - 1 and arr[right + 1] < arr[right]:
            right += 1
        
        current_peak = right - left + 1

        if longest_peak < current_peak:
            longest_peak = current_peak
        
        i = right

    return longest_peak


    
arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(arr)
print(longest_peak(arr))