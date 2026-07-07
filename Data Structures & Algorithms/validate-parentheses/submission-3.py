class Solution:
    def isValid(self, s: str) -> bool:
        s_=[]

        inter_={
            "(":")",
            "{":"}",
            "[":"]"
        }

        for i in s:
          if i in inter_:
            s_.append(i)
          else:
            if not s_:
                return False
            if inter_[s_.pop()] != i:
                return False
        
        return  not s_
            