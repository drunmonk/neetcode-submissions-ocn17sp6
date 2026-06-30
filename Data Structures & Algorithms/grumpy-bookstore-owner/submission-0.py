class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        l=0
       
        satisfied=0
        normal=0
        extr_normal=0 

        for i in range(len(customers)):
            if grumpy[i]:
                normal+=customers[i]
            else:
                satisfied+=customers[i]
            if i-l+1 >minutes:
                if grumpy[l]:
                    normal-=customers[l]
                l+=1
            extr_normal=max(extr_normal,normal)
        
        return extr_normal+satisfied
         
