class Solution:
    def isPalindrome(self, x: int) -> bool:
            list_int = list(str(x))
            reversed_list_int = list(list_int)
            reversed_list_int.reverse()

            return str(x) == ''.join(reversed_list_int)