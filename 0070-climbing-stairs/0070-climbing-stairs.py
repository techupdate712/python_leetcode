class Solution:
    def climbStairs(self, n: int) -> int:
        # if n in [1,2]:
        #     return n
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        num1 = 0
        num2 = 1
        next_number = num2 
        count = 1
        while count <= n:
            count += 1
            num1 = num2
            num2 = next_number
            next_number = num1 + num2

        return num2