class Array(object):
    def __init__(self, capacity, fill_value=None):
        self._capacity = capacity
        self._logicalSize = 0
        self._items = list()
        for count in range(capacity):
            if fill_value is not None:
                self._logicalSize += 1
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, item):
        if item < 0 or item >= self._logicalSize:
            raise IndexError
        else:
            return self._items[item]

    def __setitem__(self, key, value):
        if key < 0 or key >= self._logicalSize:
            raise IndexError
        else:
            self._items[key] = value

    def size(self):
        return self._logicalSize

    def grow(self):
        temp = Array(len(self._items) + 1)
        temp._logicalSize = self._logicalSize
        if self._logicalSize > len(self._items):
            for i in range(self._logicalSize - 1):
                temp[i] = self._items[i]
        else:
            for i in range(self._logicalSize):
                temp[i] = self._items[i]
        self._items = temp

    def shrink(self):
        if self._logicalSize <= len(self._items) // 4 and len(self._items) >= self._capacity * 2:
            temp = Array(len(self._items) // 2)
            for i in range(self._logicalSize):
                temp[i] = self._items[i]
            self._items = temp

    def insert(self, index, value):
        self._logicalSize += 1
        if self._logicalSize > len(self._items):
            self.grow()
        if index >= self._logicalSize - 1:
            self._items[self._logicalSize - 1] = value
        else:
            for i in range(self._logicalSize - 1, index, -1):
                self._items[i] = self._items[i - 1]
            self._items[index] = value

    def pop(self, index):
        if index < 0 or index >= self._logicalSize:
            raise IndexError
        value = self._items[index]
        for i in range(index, self._logicalSize - 1):
            self._items[i] = self._items[i + 1]
        self._items[self._logicalSize - 1] = None
        self._logicalSize -= 1
        return value

    def __eq__(self, other):
        if self.size() != other.size():
            return False
        for i in range(self.size()):
            if self.__getitem__(i) != other.__getitem(i):
                return False
        return True


def main():
    arr = Array(5)
    print("Array logical size is {}, Array physical size is {}".format(arr.size(), len(arr)))
    for i in range(len(arr) + 1):
        arr.insert(i, i)
    print("After insert, values in arr is:", "".join(str(arr)))
    arr.pop(2)
    print("After pop, values in arr is:", "".join(str(arr)))


if __name__ == '__main__':
    main()