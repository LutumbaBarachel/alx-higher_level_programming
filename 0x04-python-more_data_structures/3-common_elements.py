#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_elements_set = set_1 & set_2
    return common_elements_set

# Example usage:
set_1 = {'apple', 'grape', 'orange'}
set_2 = {'apple', 'grape', 'mango'}
common_elements_result = common_elements(set_1, set_2)
print(common_elements_result)
