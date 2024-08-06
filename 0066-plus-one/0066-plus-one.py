class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))  #to convert datatypes of elements in list to string
        number = ''.join(digits)
        return list(map(int,list(str(int(number)+1))))