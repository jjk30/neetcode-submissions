class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        n=len(arr)
        total=0
        count=0

        for r in range(n):
            total+=arr[r]
            if r-l+1>k:
                total-=arr[l]
                l+=1
            if r-l+1==k and threshold*k<=total:
                count+=1
        return count

        