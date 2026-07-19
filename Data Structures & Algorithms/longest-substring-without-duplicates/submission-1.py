class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        l=0
        n=len(s)
        best=0
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l+=1

            window.add(s[r])
            w=r-l+1
            best=max(best,w)
        return best

        