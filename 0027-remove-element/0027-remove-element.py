class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        countnumberofoccur = nums.count(val)
        for i in range(0,countnumberofoccur):
            nums.remove(val)
        return len(nums)        