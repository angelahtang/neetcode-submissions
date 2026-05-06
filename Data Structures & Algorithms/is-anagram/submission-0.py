class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        tLength = len(t)
        
        if sLength != tLength:
            return False
        
        sPointer = sLength-1

        while sPointer >= 0:
            sLetter = s[sPointer]
            s = s[:sPointer]
            sPointer = sPointer - 1

            tMatchPosition = t.find(sLetter)

            if tMatchPosition == -1:
                return False
            
            t = t[:tMatchPosition]+t[tMatchPosition+1:]

        return True