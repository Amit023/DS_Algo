'''
    WAF to take array as input and print it in spiral form
    Sample Input:
    arr = [ 
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
    Sample Output:
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
'''
def spiral_traverse(arr):
    
    startRow, endRow = 0, len(arr) - 1
    startCol, endCol = 0, len(arr[0]) - 1
    
    res = []

    while startRow <= endRow and startCol <= endCol:
        
        for col in range(startCol, endCol+1):
            res.append( arr[startRow][col] )
        
        for row in range(startRow + 1, endRow + 1):
            res.append( arr[row][endCol] )
        
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            res.append(arr[endRow][col])
        
        for row in reversed(range(startRow+1, endRow)):
            if startCol == endCol:
                break
            res.append(arr[row][startCol])
    
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return res


arr = [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]


arr1 = [
        [ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9],
        [10, 11, 12],
        [13, 14, 15]
    ]


print(spiral_traverse( arr ))

print(spiral_traverse( arr1 ))