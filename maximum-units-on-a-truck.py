class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        '''
        115 -> 110 (-5) -> 105 (-5) -> 98 (-7) -> 91 (-7)  
        14 -> 13        -> 12      -> 11       -> 10
        '''

        total_units = 0
        total_boxes = 0
        data = []
        for info in boxTypes:
            total_unit_per_box = info[1]
            num_of_box = info[0]
            total_units = total_units + (total_unit_per_box * num_of_box)
            total_boxes = total_boxes + num_of_box
            data.extend([total_unit_per_box]*num_of_box)

        data.sort()

        while total_boxes > truckSize:
            units_to_remove = data.pop(0)
            total_units = total_units - units_to_remove
            total_boxes = total_boxes - 1

        return total_units

            
        