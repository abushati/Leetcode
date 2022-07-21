def removeElement(self, nums: List[int], val: int) -> int:
    dups = 0
    to_check = len(nums) - 1
    index = 0 

    if len(nums)== 0:
        return dups
        print(dups)
    while to_check >= 0:
        if nums[index] == val:
            nums.pop(index)
            nums.append('_')
            dups = dups + 1
        else:
            index = index + 1

        to_check = to_check - 1
    
    return len(nums) - dups