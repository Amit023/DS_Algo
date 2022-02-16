'''
    WAP that takes input of a non-empty array of integers and return an array of same length
    Each element in the output array is equal to the product of every other number in the input array
        Note: Do not use division

    Sample Input: [ 5,  1,  4,  2]
    Sample Output: [ 8, 40, 10, 20]
'''
# Time Complexity: O(n^2) - Space Complexity: O(n)
def array_of_products(arr):
    
    res = []
    
    for i in range(len(arr)):
        product = 1
    
        for j in range(len(arr)):
            if i == j:
                continue
            product *= arr[j]
    
        res.append(product)

    return res

# Time Complexity: O(n) - Space Complexity: O(n)
def array_of_products_2(arr):
    if len(arr) <= 1:
        return arr
    
    prefix_sum = [1] * len(arr)
    postfix_sum = [1] * len(arr)

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i - 1] * arr[i - 1]
        postfix_sum[ len(arr) - (i + 1) ] = postfix_sum[ len(arr) - (i + 1) + 1 ] * arr[ len(arr) - (i + 1) + 1]
    
    # print("prefix: ",prefix_sum)
    # print("postfix: ",postfix_sum)
    res = []
    for i in range(len(arr)):
        res.append(prefix_sum[i] * postfix_sum[i])
    
    return res


print(array_of_products_2( [5, 1, 4, 2] ) )
