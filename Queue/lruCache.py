# User function Template for python3

# design the class in the most optimal way
from collections import OrderedDict


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        # code here
        self.cache = OrderedDict()
        self.capacity = cap

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    # Function for storing key-value pair.

    def set(self, key, value):
        # code here
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        # parent child info in list
        a = list(map(str, input().strip().split()))

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i+1]), int(a[i+2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i+1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends
