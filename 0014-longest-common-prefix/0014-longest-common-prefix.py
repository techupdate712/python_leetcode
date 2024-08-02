class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sortedlist = sorted(strs,key=len)
        shorteststr = sortedlist[0]
        s = ''
        flag =0
        for i in range(1,len(shorteststr)+1):
            flag = 0
            for j in strs:
                
                if shorteststr[0:i] == j[0:i]:
                    flag = flag+1
                
            if flag == len(strs):
                s = shorteststr[0:i]
        return s
