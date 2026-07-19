class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=l+((r-l)//2)
            day_used=1
            load=0
            for w in weights:
                if load+w>mid:
                    day_used+=1
                    load=0
                load+=w
            if day_used<=days:
                r=mid-1
            else:
                l=mid+1
        return l

        