class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            needed_num = target - num
            if needed_num in nums:
                try:
                    index = nums.index(needed_num)
                except: 
                    continue
                if index == i:
                    # nums.pop(index)
                    try:
                        print(nums[i+1::])
                        index2 = nums[i+1::].index(needed_num)
                        index2 = index2 + i + 1
                        return [i,index2]
                    except:  
                        pass
                    # nums.insert(needed_num, index)
                else:
                    return [i,index]