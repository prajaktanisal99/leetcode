# Merge Overlapping Sub-intervals
"""
Two intervals [L1, R1] and [L2, R2] such that L1 <= L2, are said to be overlapping if and only if L2 <= R1.
For example:
For ‘N’ = 4, and 
‘Arr’ = {{1, 3}, {2, 4}, {3, 5}, {6, 7}}
We can see that {1, 3} and {2, 4} overlap, so if we merge them, we get {1, 4}.
Now ‘Arr’ becomes: {{1, 4}, {3, 5}, {6, 7}}
Still, we observe that {1, 4} and {3, 5} overlap, hence we merge them into {1, 5}.
Hence, ‘Arr’ becomes {{1, 5}, {6, 7}}.
"""
from typing import *

def mergeOverlappingIntervals(arr):
    # Write your code here.
    current = 0

    while current < len(arr) - 1:

        if arr[current][1] >= arr[current+1][0]:
            arr[current][1] = max(arr[current][1], arr[current+1][1])
            arr.pop(current + 1)
        else:
            current += 1

    return arr

# mergeOverlappingIntervals([[1, 3], [2, 4], [3, 5], [6, 7]])
mergeOverlappingIntervals([[1, 2], [1, 3], [1, 6], [3, 4], [4, 4], [4, 5], [5, 5], [6, 6], [6, 6]])