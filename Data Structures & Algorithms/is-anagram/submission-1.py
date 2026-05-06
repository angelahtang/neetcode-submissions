class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLength = len(s)
        
        if sLength != len(t):
            return False
        
        sPointer = sLength-1            #point to end of string s
        while sPointer >= 0:
            sLetter = s[sPointer]
            s = s[:sPointer]            #last char in string s
            sPointer = sPointer - 1

            tMatchPosition = t.find(sLetter)
            if tMatchPosition == -1:    #no matching char in t
                return False
            
            t = t[:tMatchPosition]+t[tMatchPosition+1:]

        return True