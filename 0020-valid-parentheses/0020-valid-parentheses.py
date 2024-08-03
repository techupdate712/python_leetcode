class Solution:
    def isValid(self, s: str) -> bool:
        parandict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for paranthesis in s:
            if (paranthesis in parandict.keys()) and ((len(stack)==0) or (parandict[paranthesis] not in stack)):
                return False
            elif paranthesis in parandict.values():
                stack.append(paranthesis)
            else:
                
                if stack[-1] == parandict[paranthesis]:
                    print('else'+paranthesis)
                    stack.pop(-1)
        
        if len(stack) == 0:
            return True
        else:
            return False
