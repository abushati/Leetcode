class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or haystack == '':
            return 0
         
        batch_size = len(needle)
        for i in range(0,len(haystack)-batch_size+1):
            if haystack[i:i+batch_size] == needle:
                return i
        
        return -1
            
        
        
        