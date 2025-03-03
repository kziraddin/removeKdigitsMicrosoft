'''Given string num representing a non-negative integer num, and an integer k, return the smallest 
possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain 
leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
'''
class Solution(object):
    def removeKdigits(self, num, k):
        # Use a stack to build the result
        stack = []

        # Process each digit in the number
        for digit in num:
            # While stack is not empty, k > 0, and current digit is smaller than stack top
            # Remove the larger digit from stack
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If we still need to remove digits (k > 0), remove from the end
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Build the result string while removing leading zeros
        result = ''
        for digit in stack:
            if not result and digit == '0':
                continue  # Skip leading zeros
            result += digit

        # If result is empty, return "0"
        return result if result else "0"