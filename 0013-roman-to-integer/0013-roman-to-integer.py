class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        specialromandict = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        num =0
        for i in list(specialromandict.keys()):
            if i in s:
                z = s.count(i)
                num = num + z*specialromandict[i]
                s = s.replace(i,'')
        
        for i in list(romandict.keys()):
            if i in s:
                z = s.count(i)
                num = num + z*romandict[i]
                s = s.replace(i,'')
        return num
        