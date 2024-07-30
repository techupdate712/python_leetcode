class Solution:
    def isPalindrome(self, x: int) -> bool:
        y =  list(str(x))
        left = 0
        right = len(y)-1
        while(left<=right):
            if y[left] == y[right]:
                left = left+1
                right = right -1
            else:
                return False
        return True