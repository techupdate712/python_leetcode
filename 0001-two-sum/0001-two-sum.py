class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            y = target - nums[i]
            if y in nums[i + 1 :]:
                return [i, nums.index(y, i + 1)]
            else:
                continue
        return []