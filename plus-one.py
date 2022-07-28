class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(d) for d in digits]))
        num = num + 1
        return [int(i) for i in str(num) ]
        