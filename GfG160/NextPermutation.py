"""
    Given an array of integers arr[] representing a permutation,
    implement the next permutation that rearranges the numbers 
    into the lexicographically next greater permutation. 
    If no such permutation exists, rearrange the numbers
    into the lowest possible order (i.e., sorted in ascending order). 

    Note:  A permutation of an array of integers refers to
    a specific arrangement of its elements in a sequence or linear order.
"""

class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1
        #find pivot (the rightest element where i<i+1)
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                pivot = i
                break
        if pivot == -1:
            arr.reverse()
            return
        
        #find rightest number greater than pivot
        j = n-1
        while arr[j] <= arr[pivot]:
            j-=1
        
        #swap
        arr[j], arr[pivot] = arr[pivot], arr[j]
        
        #reverse remaining elements
        start = pivot +1
        end = n-1
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
        