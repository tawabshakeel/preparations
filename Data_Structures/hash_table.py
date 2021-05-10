class HashTable:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.arr[index] = val

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None


if __name__ == '__main__':
    h1 = HashTable()
    print(h1.get_hash("tawab"))
    h1['tawab'] = 1
    print(h1.arr)