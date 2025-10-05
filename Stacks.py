#Last In,   First Out
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, node):
        self.data.append(node)
    
    def pop(self):
        self.data.pop()

""" Use cases 
- backtracking
- memory managment in compilers
- DFS

"""
# Tests