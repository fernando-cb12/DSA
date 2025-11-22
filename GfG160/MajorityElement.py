"""
    Given an array arr[] consisting of n integers, the task is to 
    find all the array elements which occurs more than floor(n/3) times.

    Note: The returned array of majority elements should be sorted.
"""

class Solution:
    def findMajority(self, arr):

        n= len(arr)
        freq = {}
        result = []
        # Use a hashmap to get frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # iterate over freq to get the elements which occur more than floor(n/3)
        for num, value in freq.items():
            if value > n//3:
                result.append(num)
            
        
        if len(result) > 1:
            result.sort()
        
        
        return result
                