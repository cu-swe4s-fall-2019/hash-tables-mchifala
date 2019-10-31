import hash_functions


class LinearProbe:
    """
    This class is used to represent a hash table that uses linear
    probing as a collision strategy

    Attributes:
    - hash_function: h_ascii, h_rolling, or h_mult
    - n(int): The hash table size
    - table(list): The actual hash table itself
    - m(int): The number of elements in the hash function

    Methods:
    - add(self, key, value): This function adds a key-value pair
                             to the hash table
    - search(self, key): This function searchs for a key in the
                         hash table

    """
    def __init__(self, n, hash_function):
        self.hash_function = hash_function
        self.n = n
        self.table = [None for i in range(n)]
        self.m = 0
        self.keys = []

    def add(self, key, value):
        """
        This function adds a key-value pair to the hash table

        Parameters:
        - key(str): The key we wish to hash
        - value(str): The value we wish to store

        Returns:
        - True or False

        """
        start_hash = self.hash_function(key, self.n)

        for i in range(self.n):
            test_slot = (start_hash + i) % self.n
            if self.table[test_slot] is None:
                self.table[test_slot] = (key, value)
                self.keys.append(key)
                self.m += 1
                return True

        return False

    def search(self, key):
        """
        This function searchs for a key in the hash table

        Parameters:
        - key(str): The key we wish to find

        Returns:
        - The value of the desired key or None

        """
        start_hash = self.hash_function(key, self.n)

        for i in range(self.n):
            test_slot = (start_hash + i) % self.n

            if self.table[test_slot] is None:
                return None

            if self.table[test_slot][0] == key:
                return self.table[test_slot][1]

        return None


class ChainedHash:
    """
    This class is used to represent a hash table that uses
    chaining as a collision strategy

    Attributes:
    - hash_function: h_ascii, h_rolling, or h_mult
    - n(int): The hash table size
    - table(list): The actual hash table itself
    - m(int): The number of elements in the hash function

    Methods:
    - add(self, key, value): This function adds a key-value pair
                             to the hash table
    - search(self, key): This function searchs for a key in the
                         hash table

    """
    def __init__(self, n, hash_function):
        self.hash_function = hash_function
        self.n = n
        self.table = [[] for i in range(n)]
        self.m = 0
        self.keys = []

    def add(self, key, value):
        """
        This function adds a key-value pair to the hash table

        Parameters:
        - key(str): The key we wish to hash
        - value(str): The value we wish to store

        Returns:
        - True or False

        """
        hash_slot = self.hash_function(key, self.n)
        self.table[hash_slot].append((key, value))
        if key not in self.keys:
            self.keys.append(key)
        self.m += 1
        return True

    def search(self, key):
        """
        This function searchs for a key in the hash table

        Parameters:
        - key(str): The key we wish to find

        Returns:
        - The value of the desired key or None

        """
        hash_slot = self.hash_function(key, self.n)
        for data in self.table[hash_slot]:
            if data[0] == key:
                return data[1]

        return None
