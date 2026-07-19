class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best=0
        l=0
        count=[0]*26
        n=len(s)
        for r in range(n):
            count[ord(s[r])-65]+=1
         
            while r-l+1 - max(count)>k: # bigger than k
                count[ord(s[l])-65]-=1
                l+=1
            best=max(best,r-l+1)
        return best
