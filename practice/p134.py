


# sparse array


class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self.map = {}
        for i in range(len(arr)):
            if arr[i] != 0:
                self.map[i] = arr[i]
    
    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError()
        self.map[i] = val

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError()
        val = self.map.get(i)
        if val is None:
            return 0
        return val