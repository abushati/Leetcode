class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(1,numRows+1):
            new_row = []
            print(tri)
            print(i)
            if i in [1,2]:
                new_row.extend([1]*i)
            else:
                print(tri)
                pre_row = tri[i-2]
                for i in range(0,len(pre_row)-1):
                    first_num = pre_row[i]
                    second_num = pre_row[i+1]
                    new_row.append(first_num+second_num)
                new_row.insert(0,1)
                new_row.insert(len(pre_row), 1)
                
            tri.append(new_row)
            
        
        return tri