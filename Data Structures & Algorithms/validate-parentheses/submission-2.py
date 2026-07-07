class Solution:
    def isValid(self, s: str) -> bool:
        s_=[]

        inter_={
            "(":")",
            "{":"}",
            "[":"]"
        }

        for i in s:
            if s_ :
                if s_[-1] not in inter_:
                    return False
                if inter_[s_[-1]]==i:
                  s_.pop()
                else:
                  s_.append(i)
            else:
                s_.append(i)
        return len(s_) ==0