"""
    Just for fun, the following Python code does a brute force check to see if any
    permutation of the series will yeild a result greater than 32. 

    If will first generate a list of all possible permuations, then iterate through them.
    For each permuation, it will set 3 variables to be the 3 consecutive numbers to add. 
    It will first set them to be the last two at the end of the array to account for 
    the situation where you're counting numbers from the end and the beginning of the array.

    While the proof is obviously a much better way to show this, the brute force 
    coding method is fun nonetheless. 
"""

import itertools

nums = range(1,20,2)
perms = itertools.permutations(nums)

def noneLessThan32(perms):
    for perm in list(perms):
        series = [0, perm[-2], perm[-1]]
        allLess = True
        for x in perm:
            series = [series[1], series[2], x]
            if sum(series) >= 32:
                allLess = False
                break

        if allLess:
            return False
    return True

print("None are less than 32: " + str(noneLessThan32(perms)))