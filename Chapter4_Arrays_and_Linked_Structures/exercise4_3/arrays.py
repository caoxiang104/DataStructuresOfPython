class Array(object):
    def __init__(self, capacity, fill_value=None):
        self._items = list()
        self.logical_size = 0
        self.capacity = capacity
        for i in range(capacity):
            self._items.append(fill_value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        if value is not None:
            self.logical_size += 1
        self._items[key] = value

    def insert(self, index, value):
        if self.logical_size == self.capacity:
            temp = Array(self.capacity * 2)
            for i in range(self.capacity):
                temp[i] = self._items[i]
            self._items = temp
            self.capacity *= 2
        for i in range(self.logical_size, index, -1):
            self._items[i] = self._items[i - 1]
        self._items[index] = value
        self.logical_size += 1

    def delete(self, index):
        for i in range(index, self.logical_size - 1):
            self._items[i] = self._items[i + 1]
        self._items[self.logical_size - 1] = None
        self.logical_size -= 1


def main():
    array = Array(5)
    for i in range(5):
        array[i] = i
    array.insert(3, 8)
    print(array.logical_size)
    print(array)
    array.delete(2)
    print(array)
    print(array.capacity)


if __name__ == '__main__':
    main()

