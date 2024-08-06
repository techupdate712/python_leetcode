class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums,target)
        return i