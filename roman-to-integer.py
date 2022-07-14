class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_numeral = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M': 1000}

        skip_next_special = False
        int_lists = []


        for i,char in enumerate(s):
            if skip_next_special:
                skip_next_special = False
                continue

            try:
                next_char =  s[i+1]
            except:
                next_char = None 

            if char == 'I' and  next_char in ('V','X'):
                skip_next_special = True 
                if next_char == "V":
                    int_char = 4
                elif next_char	== 'X':
                    int_char = 9		
            elif char == 'X' and  next_char in ('L','C'):
                skip_next_special = True 
                if next_char == "L":
                    int_char = 40
                elif next_char	== 'C':
                    int_char = 90
            elif char == 'C' and  next_char in ('D','M'):
                skip_next_special = True 
                if next_char == "D":
                    int_char = 400
                elif next_char	== 'M':
                    int_char = 900
            else:
                skip_next_special = False
                int_char = roman_to_numeral.get(char)

            int_lists.append(int_char)


        output = 0
        for i in int_lists:
            output = output+i

        # print(output)
        return output

      #CLEAN VERSION
      class Solution:
    def romanToInt(self, s: str) -> int:

        roman_to_numeral = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M': 1000}
        special_combos = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        special_combos_chars = special_combos.keys()
        
        skip_next_special = False
        int_lists = []


        for i,char in enumerate(s):
            if skip_next_special:
                skip_next_special = False
                continue

            try:
                next_char =  s[i+1]
            except:
                next_char = '' 
            
            combo_check = char+next_char
            if combo_check in special_combos_chars:
                skip_next_special = True
                int_char = special_combos.get(combo_check)
            else:
                skip_next_special = False
                int_char = roman_to_numeral.get(char)

            int_lists.append(int_char)


        output = 0
        for i in int_lists:
            output = output+i

        # print(output)
        return output