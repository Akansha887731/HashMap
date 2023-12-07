"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1
"""

# Solution 1 : With hash map
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n)) 
        return n == 1 

# Solution 2 : Withput Hash map
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()    
        while n:
            square_sum = 0
            while n:
                r = n % 10
                n = n // 10
                square_sum += r ** 2
            if square_sum == 1:
                return True
            if square_sum in seen:
                return False
            seen.add(square_sum)
            n = square_sum
        return False

        

