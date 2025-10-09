"""
Given an array of positive integers arr[], 
return the second largest element from the 
array. If the second largest element doesn't
exist then return -1.

Note: The second largest element should not 
be equal to the largest element.
"""

class Solution:
    def getSecondLargest(self, arr):
        largest = -1
        second = -1
        # Code Here
        for i in range(len(arr)):
            if arr[i] > largest:
                second = largest
                largest = arr[i]
            elif (arr[i] < largest and arr[i] > second):
                second = arr[i]
        return second