class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [1, 1]

        i = 0
        checked_index = 0
        length_nums = len(nums) - 1

        if length_nums == 0:
            return 1
            # print(nums)

        while checked_index <= length_nums:
            checked_index = checked_index + 1

            if i > 0 and nums[i-1] == nums[i]:
                # print(i)
                # print(nums)
                nums.pop(i)
                nums.append('_')
                continue

            i = i + 1

        return i
        # print(nums)