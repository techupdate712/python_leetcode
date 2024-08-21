class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.sumarr = self.nums
        self.sumarrprefix()

    def sumarrprefix(self):
        self.sumarr[0] = self.nums[0]
        n = len(self.nums)
        for i in range(1,n):
            self.sumarr[i] = self.sumarr[i-1]+self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sumarr[right]
        else:
            return self.sumarr[right] - self.sumarr[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)