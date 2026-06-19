class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        marg=0

        i=0
        j=1
        p=0
        while i <len(prices) and j<len(prices):
            if prices[j]-prices[i] >0:
               p= max(p,prices[j]-prices[i])
               j+=1
            else:
                i=j
                j+=1
        return p
           
