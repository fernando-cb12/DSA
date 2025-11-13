
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left<= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1


array = [0, 1, 3, 4, 6, 7, 9, 11, 12, 15, 16, 18, 20, 21, 22]
target = 3
print(binary_search(array, target))
