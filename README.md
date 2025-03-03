# Remove K Digits

Given a string `num` representing a non-negative integer and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

## Problem Examples
1. **Input**: `num = "1432219"`, `k = 3`  
   **Output**: `"1219"`  
   **Explanation**: Remove 4, 3, and one 2 to form the smallest number 1219.

2. **Input**: `num = "10200"`, `k = 1`  
   **Output**: `"200"`  
   **Explanation**: Remove the leading 1, result is 200 (no leading zeros).

3. **Input**: `num = "10"`, `k = 2`  
   **Output**: `"0"`  
   **Explanation**: Remove both digits, resulting in 0.

## Constraints
- 1 <= k <= num.length <= 10⁵
- `num` consists of only digits.
- `num` has no leading zeros except for the zero itself.

## Solution
The solution uses a greedy approach with a monotonic stack to remove digits that create "peaks" (larger digits followed by smaller ones), ensuring the smallest possible result.

```python
def removeKdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    while k > 0 and stack:
        stack.pop()
        k -= 1
    
    result = ''
    for digit in stack:
        if not result and digit == '0':
            continue
        result += digit
    
    return result if result else "0"

Example Walkthroughs

Example 1: num = "1432219", k = 3
Goal: Remove 3 digits to get the smallest number.

Initial State

Stack: []
k: 3

Steps

Digit '1'
Stack empty, push '1'.
Stack: [1], k: 3

Digit '4'
Top (1) < 4, push '4'.
Stack: [1, 4], k: 3

Digit '3'
Top (4) > 3 and k > 0, pop '4'.
Stack: [1], k: 2
Push '3'.
Stack: [1, 3], k: 2

Digit '2'
Top (3) > 2 and k > 0, pop '3'.
Stack: [1], k: 1
Push '2'.
Stack: [1, 2], k: 1

Digit '2'
Top (2) = 2, push '2'.
Stack: [1, 2, 2], k: 1

Digit '1'
Top (2) > 1 and k > 0, pop '2'.
Stack: [1, 2], k: 0
Push '1'.
Stack: [1, 2, 1], k: 0

Digit '9'
k = 0, push '9'.
Stack: [1, 2, 1, 9], k: 0

Post-Processing
k = 0, no extra removals.
Result: "1219"
Output
"1219"


Example 2: num = "10200", k = 1
Goal: Remove 1 digit to get the smallest number.

Initial State
Stack: []
k: 1
Steps
Digit '1'
Stack empty, push '1'.
Stack: [1], k: 1
Digit '0'
Top (1) > 0 and k > 0, pop '1'.
Stack: [], k: 0
Push '0'.
Stack: [0], k: 0
Digit '2'
k = 0, push '2'.
Stack: [0, 2], k: 0
Digit '0'
k = 0, push '0'.
Stack: [0, 2, 0], k: 0
Digit '0'
k = 0, push '0'.
Stack: [0, 2, 0, 0], k: 0
Post-Processing
k = 0, no extra removals.
Result: "0200" → "200" (strip leading zeros).
Output
"200"


Example 3: num = "10", k = 2
Goal: Remove 2 digits to get the smallest number.

Initial State
Stack: []
k: 2
Steps
Digit '1'

Stack empty, push '1'.
Stack: [1], k: 2

Digit '0'
Top (1) > 0 and k > 0, pop '1'.
Stack: [], k: 1
Push '0'.
Stack: [0], k: 1

Post-Processing
k = 1, pop '0'.
Stack: [], k: 0
Result: "" → "0" (empty case).
Output
"0"

Key Points
Time Complexity: O(n) - each digit is pushed and popped at most once.
Space Complexity: O(n) - stack stores up to n digits.
Greedy Logic: Remove larger digits when followed by smaller ones to minimize the number.
Edge Cases: Handles leading zeros and empty results correctly.
