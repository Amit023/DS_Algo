'''
    Return minimum amount of money you cannot create with the coins
    Sample Input: 
        coins = [1, 2, 5, 6]
    Sample Output: 4

    Sample Input: [5, 7, 1, 1, 2, 3, 22]
    Sample Output: 20
'''
def non_constructible_change(coins):
    coins.sort()

    coin_sum  = 0
    for i in coins:
        if coin_sum + 1 < i:
            return coin_sum + 1
        coin_sum += i
    
    return coin_sum+1


coins = [5, 7, 1, 1, 2, 3, 22]

print( non_constructible_change(coins))