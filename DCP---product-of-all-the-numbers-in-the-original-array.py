
def get_new_array(n):
    new_array = [0]*len(n)
    for i, _ in enumerate(n):
        new_array_value = 1
        for a, value2 in enumerate(n):
            if a == i:
                continue
            new_array_value = new_array_value * value2
        new_array[i] = new_array_value

    return new_array
        

test_arrays = [[3, 2, 1], [1, 2, 3, 4, 5]]
for arr in test_arrays:
    new_arr = get_new_array(arr)
    print(f'Input arr {arr}, Output arr {new_arr}')
    
    
    
    
    
 class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:

        
        length = len(n)
        left = [1] * length
        for i in range(1,length):
            left[i] = left[i-1] * n[i-1]
        # print(left)
        
        right = [1] * length
        for i in range(length-1,0,-1):
            right[i-1] = right[i] * n[i]

        
        output = []
        for i in range(length):
            output.append(left[i]*right[i])
        
        return output
        
        
