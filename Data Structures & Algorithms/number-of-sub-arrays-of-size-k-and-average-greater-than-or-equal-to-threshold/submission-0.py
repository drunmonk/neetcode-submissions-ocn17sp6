class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        

        i=0
        j=k-1
        s=0
        for f in range(k):
            s+=arr[f]
        
        n=0
        
        while j<len(arr):
            if (s/k)>=threshold:
                n+=1
            i+=1
            j+=1
            if j<len(arr):
              s=(s-arr[i-1])+arr[j]
            

        return n

            