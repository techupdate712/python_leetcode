class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a= int(a,2)
        b= int(b,2)
        return str(format(a+b,'b'))