class Solution:
    def canJump(self, nums: List[int]) -> bool:
        values=0
        n=len(nums)
        for i in range(n):
            if i>values:
                return False
            values=max(values,i+nums[i])
        return True
        