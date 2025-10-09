""" Dictionary
    - Generic way to map keys to values
    Hash table
    - Implementation of a dictionary using a hash function
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hashFunction(self, key):
        #hash by division
        return hash(key) % self.size
    
    def insert(self, key, value):
        
        # Insert key-value pair into the hash table
        index = self.hashFunction(key)  # Calculate the index using the hash function
        if self.table[index] is None:  
            # If there is no entry at the index, insert the value directly
            self.table[index] = (key, value)
        else:
            # Handle collisions by chaining (storing multiple key-value pairs at the same index)
            current_key, current_value = self.table[index]
            if current_key == key:
                # If the key already exists, update the value
                self.table[index] = (key, value)
            else:
                # Collision resolution: store as a list of tuples
                self.table[index] = [(current_key, current_value), (key, value)]

    def search(self, key):
        # Search for a value by key
        index = self.hashFunction(key)
        if self.table[index] is None:
            return None  # No item at that index
        elif isinstance(self.table[index], list):
            # Handle chaining: search through the list of key-value pairs
            for k, v in self.table[index]:
                if k == key:
                    return v
        else:
            # Direct match for a single key-value pair
            return self.table[index][1]

    def delete(self, key):
        # Remove a key-value pair from the table
        index = self.hashFunction(key)
        if self.table[index] is None:
            return False  # No item at that index
        elif isinstance(self.table[index], list):
            # Handle chaining: search and remove key-value pair
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    if not self.table[index]:
                        self.table[index] = None  # Remove the list if it's empty
                    return True
        else:
            # Direct match for a single key-value pair
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            return False