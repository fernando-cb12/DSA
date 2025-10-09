"""
You are given an array of integers arr[]. 
You have to reverse the given array.
Note: Modify the array in place.
"""

class Solution:
    def reverseArray(self, arr):
        # code here
        i = 0
        j = len(arr) - 1
        
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        
        