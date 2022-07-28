class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        found_first_char = False
        count = 0
        for i,char in enumerate(s[::-1]):
            if (char == " " or i == 0) and found_first_char:
                break
            if char == " ":
                continue
            found_first_char = True
            count += 1
            
        return count