class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = list(sorted(set(nums)))
        k = len(x)
        nums[0:k] = x[0:k]
        return k