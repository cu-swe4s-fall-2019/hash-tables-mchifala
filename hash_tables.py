import hash_functions

class LinearProbe:
    def __init__(self, n, hash_function):
        self.hash_function = hash_function
        self.n = n
        self.table = [ None for i in range(n) ]
        self.m = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.n)
        
        for i in range(self.n):
            test_slot = (start_hash + i) % self.n
            if self.table[test_slot] == None:
                self.table[test_slot] = (key, value)
                self.m +=1
                return True
            
        return False
                
    def search(self, key):
        start_hash = self.hash_function(key, self.n)
        
        for i in range(self.n):
            test_slot = (start_hash + i) % self.n

            if self.table[test_slot] == None:
                return None

            if self.table[test_slot][0] == key:
                return self.table[test_slot][1]

        return None

class ChainedHash:
    def __init__(self, n, hash_function):
        self.hash_function = hash_function
        self.n = n
        self.table = [ [] for i in range(n) ]
        self.m = 0

    def add(self, key, value):
        hash_slot = self.hash_function(key, self.n)
        self.table[hash_slot].append((key,value))
        self.m +=1
        return True

    def search(self, key):
        hash_slot = self.hash_function(key, self.n)
        for data in self.table[hash_slot]:
            if data[0] == key:
                return data[1]

        return None


