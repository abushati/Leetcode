
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