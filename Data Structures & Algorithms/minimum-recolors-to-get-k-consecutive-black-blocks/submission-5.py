class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c_w=0
        i=0
        j=k

        for i in range(k):
            if blocks[i] =='W':
                c_w+=1
            i+=1

        min_con=c_w
         
        i=0

        while i <j and j<len(blocks):
            if blocks[i] =='W':
                c_w-=1
            
            if blocks[j]=='W':
                c_w+=1 
            i+=1
            j+=1
            
            min_con=min(min_con,c_w)
        
        return min_con




        