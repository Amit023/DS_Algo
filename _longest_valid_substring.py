'''
Given a string consisting of opening and closing parenthesis,
find length of the longest valid parenthesis substring.
    Sample Input: ")()(()(("
    Sample Output: 2 "()"
    
    Sample Input: ")()())"
    Sample Output: 4 "()()"

    Sample Input: "))(()())(((((("
    Sample Output: 6 "(()())"
'''

# Use Stack to keep track of valid substring
# Time Complexity: O(N^2), Space Complexity: O(N)
def longest_valid_substring(s):
    
    stack = [-1]
    res = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()

            if len(stack) == 0:
                stack.append(i)
            else:
                res = max(res, i - stack[len(stack) - 1])
    return res


# Use left and right to keep track of opening and closing bracket
# Time Complexity: O(N) Space Complexity: O(1)
def longest_valid_substring_2(s):
    left, right, res = 0, 0, 0

    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            res = max(res, 2 * left)
        elif right > left:
            left = right = 0
    
    left = right = 0

    
    for i in reversed(s):
        if i == '(':
            left += 1
        else:
            right += 1

        if left == right:
            res = max(res, 2 * left)
        elif left > right:
            left = right = 0

    print("****",res)
    return res


print(longest_valid_substring_2(")()(()(("))
print(longest_valid_substring_2(")()())"))
print(longest_valid_substring_2("))(()())(((((("))