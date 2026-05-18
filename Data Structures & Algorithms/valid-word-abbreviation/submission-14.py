class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        m=len(word)
        n=len(abbr)

        i=0
        j=0

        while i <m and j<n:

            if abbr[j]=='0':
                return False
            elif word[i]==abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isalpha():
                return False
            else:
                l=0
                while j<n and abbr[j].isdigit():
                    l=l*10+int(abbr[j])
                    j+=1
                i+=l
        return i==m and j ==n
            