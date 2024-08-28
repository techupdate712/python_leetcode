class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        sqlist = []
        while(left<=right):
            if nums[left]*nums[left] > nums[right]*nums[right]:
                sqlist.append(nums[left]*nums[left])
                left = left + 1
            else:
                sqlist.append(nums[right]*nums[right])
                right = right - 1
        sqlist.reverse()
        return sqlist