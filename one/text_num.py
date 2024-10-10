import re

def extractNums(input_string):
    nums = []

    for char in input_string:
        if char.isnumeric():
            nums.append(int(char))
    return {
        'output': nums
        }

 