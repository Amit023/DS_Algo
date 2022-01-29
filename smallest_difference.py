''''
    Sample Input: 
        arrOne = [-1, 5, 10, 20, 28, 3]
        arrTwo = [26, 134, 135, 15, 17]

    Sample Output:
        [28, 26]
'''

# Brute Force Algorithm
# Time Complexity: O(N^2)
def smallest_difference(arrOne, arrTwo):
    smallest_diff = []
    global_diff = 1000

    for i in range(len(arrOne)):# O(N)
        for j in range(len(arrTwo)):# O(N)
            if abs(arrOne[i] - arrTwo[j]) < global_diff:
                smallest_diff = [arrOne[i], arrTwo[j]]
                global_diff = abs(arrOne[i] - arrTwo[j])

    return smallest_diff



def smallest_difference_2(arrOne, arrTwo):
    idx1, idx2 = 0, 0
    g_diff, diff = float('inf'), float('inf')
    smallest_pair = []

    while idx1 < len(arrOne) and idx2 < len(arrTwo): # O(N + M)
        num1, num2 = arrOne[idx1], arrTwo[idx2]

        if num1 < num2:
            diff = abs(num2 - num1)
            idx1 += 1
        elif num2 < num1:
            diff = abs(num1 - num2)
            idx2 += 1
        else:
            return [num1, num2]

        if g_diff > diff:
            g_diff = diff
            smallest_pair = [num1, num2]
    
    return smallest_pair

arrOne = [-1, 5, 10, 20, 28, 3]
arrTwo = [26, 134, 135, 15, 17]

print(smallest_difference_2(arrOne, arrTwo))