from Chapter11_Sets_and_Dicts.abstractset import AbstractSet
from Chapter10_Trees.linkedbst import LinkedBST, LinkedStack
from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection


class TreeSortedSet(AbstractionCollection, AbstractSet):
    """A tree-based implementation of a sorted set"""

    def __init__(self, sourceCollection=None):
        self._items = LinkedBST()
        AbstractionCollection.__init__(self, sourceCollection)

    def __contains__(self, item):
        """Returns True of item is in the set or False otherwise."""
        if self._items.find(item):
            return True
        else:
            return False

    def __iter__(self):
        stack = LinkedStack()
        stack.push(self._items._root)
        while not stack.isEmpty():
            node = stack.pop()
            yield node.data
            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)

    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if item not in self:
            self._items.add(item)
            self._size += 1


def main():
    tree_sort_set = TreeSortedSet()
    for i in range(10):
        tree_sort_set.add(i)
    print(tree_sort_set)



if __name__ == '__main__':
    main()