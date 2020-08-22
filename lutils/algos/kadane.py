'''
Created Date: Wednesday August 19th 2020
Author: Leo Tran (Tran Duc Loi)
-----
Last Modified: Wednesday August 19th 2020 10:33:20 pm
Modified By: Leo Tran (Tran Duc Loi)
-----
HISTORY:
Date      	By    	Comments
----------	------	---------------------------------------------------------
21-08-2020	loitd	Initialize the file
'''

# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

def maxsum(sequence):
    """Return maximum sum."""
    maxsofar, maxendinghere = 0, 0
    for x in sequence:
        # invariant: ``maxendinghere`` and ``maxsofar`` are accurate for ``x[0..i-1]``          
        maxendinghere = max(maxendinghere + x, 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar

print(maxsum([1,-1,3,4,5,-9,-10]))
print(maxsum([3,7,4,6,5])==13)
# print(maxsum([3,5,-7,8,10])==15)
# print(maxsum([3,5,-7,8,10])==15)

