from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class Heap(AbstractionCollection):
    """An list-based heap implement."""

    def __init__(self, sourceCollection=None):
        self._heap = list()
        AbstractionCollection.__init__(self, sourceCollection)

    def add(self, item):
        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1
        while curPos > 0:
            parent = (curPos - 1) // 2
            parenItem = self._heap[parent]
            if parenItem <= item:
                break
            else:
                self._heap[curPos] = self._heap[parent]
                self._heap[parent] = item
                curPos = parent

    def pop(self):
        if self.isEmpty():
            raise Exception("Heap is empty")
        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)
        if len(self._heap) == 0:
            return bottomItem
        self._heap[0] = bottomItem
        lastIndex = len(self._heap) - 1
        curPos = 0
        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2
            if leftChild > lastIndex:
                break
            if rightChild > lastIndex:
                maxChild = leftChild
            else:
                leftItem = self._heap[leftChild]
                rightItem = self._heap[rightChild]
                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild
            maxItem = self._heap[maxChild]
            if bottomItem <= maxItem:
                break
            else:
                self._heap[curPos] = self._heap[maxChild]
                self._heap[maxChild] = bottomItem
                curPos = maxChild
        return topItem

    def __iter__(self):
        cur = 0
        while cur < self._size:
            yield self._heap[cur]
            cur += 1


def main():
    heap = Heap()
    heap.add(4)
    heap.add(3)
    heap.add(5)
    heap.add(6)
    heap.add(1)
    heap.add(2)
    heap.add(7)
    print("Heap:", str(heap))
    heap.pop()
    print("After pop:", heap)
    a = list()
    while not heap.isEmpty():
        a.append(heap.pop())
    print("Sort:", str(a))




if __name__ == '__main__':
    main()
