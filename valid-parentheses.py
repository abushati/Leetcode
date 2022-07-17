list_s = list(s)
pairs = {'(':')','[':']','{':'}'}


LIFO = []
for c in s:
    if c in pairs.keys():
        LIFO.append(c)
        continue
    start_sym_to_find = None
    for key, value in pairs.items():
        if value == c:
            start_sym_to_find = key

    try:
        last_element = LIFO[-1]
    except:
        last_element = None

    if start_sym_to_find == last_element:
        LIFO.pop(-1)
    else:
        return False

if LIFO:
    return False

return True