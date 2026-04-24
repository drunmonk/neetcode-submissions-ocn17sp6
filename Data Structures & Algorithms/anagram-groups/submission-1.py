class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        di={}
        for i in strs:
            _interm=[0]*26
            for j in i:
                a_=ord(j)-ord('a')
                _interm[a_]+=1
            if tuple(_interm) in di:
                di[tuple(_interm)].append(i)
            else:
                di[tuple(_interm)]=[i]
        return list(di.values())

