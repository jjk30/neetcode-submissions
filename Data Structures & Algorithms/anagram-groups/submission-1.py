from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for character in s:
                count[ord(character)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())


        