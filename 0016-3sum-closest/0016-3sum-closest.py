class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        closestsum = 99999
        nums.sort()
        for i in range(0,len(nums)-2):
            f1 = nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                sum = f1 + nums[left]+nums[right]
                closestsum = min([sum,closestsum], key= lambda x:abs(x-target))
                if sum>target:
                    right = right-1
                else:
                    left = left+1
        return closestsum
            