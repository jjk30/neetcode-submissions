class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        best=float("inf")
        n=len(nums)
        for r in range(n):
            total+=nums[r]
            while total>=target:
                best=min(best,r-l+1)
                total-=nums[l]
                l+=1

        return 0 if best==float("inf") else best
            
        