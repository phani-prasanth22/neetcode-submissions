class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = float("-inf")
        i = 0
        j = len(heights)-1
        while(i<j):
            hi = min(heights[i],heights[j])
            wi = j-i
            cw = hi*wi
            maxi = max(cw,maxi)

            if(heights[i] > heights[j]):
                j-=1
            else:
                i+=1
        return maxi
            


        