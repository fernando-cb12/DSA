"""
    Heaps start with index 1
    Use cases: Heap sort, trees, Priority queues.
"""

class Heap:
    def __init__(self):
        self.data = [None]
        self.size = 0 # initial value to not include None value



    def maxHeapify(self, i):
        arr = self.data
        l = 2 * i
        r = 2 * i + 1
        heap_size = self.size
        largest = i

        if l <= heap_size and arr[l] > arr[largest]:
            largest =  l
        if r <= heap_size and arr[r] > arr[largest]:
            largest = r
        # Recursive call
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.maxHeapify(largest)

    #HeapifyWrapper
    def buildMaxHeap(self, arr):
        self.data = [None] + arr #add None to match one-based index
        self.size = len(arr)
        #bottom-up approach
        for leaves in range(self.size//2, 0, -1):
            self.maxHeapify(leaves)


heap = Heap()
arr = [4, 10, 3, 5, 1]
heap.buildMaxHeap(arr)


print(heap.data[1:])