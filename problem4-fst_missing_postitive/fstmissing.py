"""
    From question we know, the input will be an unsorted integer array, so the input cannot be empty.
"""
def fst_missing(self, input_list):# Our original array  
    input_list.sort()
    res = 1
    for num in input_list:
        if num == res:
            res += 1
    return res  
