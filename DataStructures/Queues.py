from collections import deque
""" This library imports a doubly linked list
    where we add elements from the back
    and remove them from the front of the queue
    First in, First Out
"""
class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        self.data.popleft()

""" Examples
    -Spotify Queue
    -CPU scheduling
    -BFS 
"""