class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for n in s:
            ds[n] = ds.get(n,0) + 1
        for n in t:
            dt[n] = dt.get(n,0) + 1

        if dt == ds:
            return True
        return False

        
        
