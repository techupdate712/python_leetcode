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
        
#Easy Solution
# def isPalindrome(self, x: int) -> bool:
# 	if x < 0:
# 		return False
	
# 	return str(x) == str(x)[::-1]

#If we don't want to convert the number to string, then recreate a new number in reverse order.
# def isPalindrome(self, x: int) -> bool:
# 	if x<0:
# 		return False

# 	inputNum = x
# 	newNum = 0
# 	while x>0:
# 		newNum = newNum * 10 + x%10
# 		x = x//10
# 	return newNum == inputNum
