from Chapter6_Inheritance_and_Abstract_Classes.abstractcollection import AbstractionCollection
from Chapter10_Trees.bstnode import BSTNode
from Chapter8_Queues.linkedqueue import LinkedQueue
from Chapter7_Stacks.linkedstack import LinkedStack
from math import log


class LinkedBST(AbstractionCollection):
    """A link-based binary search tree implement."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the contents of
        sourceCollection, if it's present."""
        self._root = None
        AbstractionCollection.__init__(self, sourceCollection)

    def find(self, value):
        """Returns data if value is found of None otherwise."""

        # Helper function to search the binary tree.
        def recurse(node):
            if node is None:
                return None
            elif value == node.data:
                return node.data
            elif value < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        # Top level call on the root node
        return recurse(self._root)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postorder(self):
        """Supports an postorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """Supports an levelorder traversal on a view of self."""
        lyst = list()
        queue = LinkedQueue()

        def recurse(queue):
            if not queue.isEmpty():
                temp = queue.pop()
                lyst.append(temp.data)
                if temp.left is not None:
                    queue.add(temp.left)
                if temp.right is not None:
                    queue.add(temp.right)
                recurse(queue)
        if self._root is not None:
            queue.add(self._root)
            recurse(queue)
        return iter(lyst)

    def preorder(self):
        """Supports an preorder traversal on a view of self."""
        lyst = list()
        stack = LinkedStack()

        def recurse(stack):
            if not stack.isEmpty():
                temp = stack.pop()
                lyst.append(temp.data)
                if temp.right is not None:
                    stack.push(temp.right)
                if temp.left is not None:
                    stack.push(temp.left)
                recurse(stack)
        if self._root is not None:
            stack.push(self._root)
            recurse(stack)
        return iter(lyst)

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "|" * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def remove(self, value):
        root = self._root
        if value not in self:
            raise KeyError("Item not in tree.""")

        def findMaxValueInLeftSubtree(node):
            father_node = node
            child_node = node.left
            while child_node.right is not None:
                father_node = child_node
                child_node = child_node.right
            node.data = child_node.data
            if father_node is node:
                father_node.left = child_node.left
            else:
                father_node.right = child_node.left

        def find_node(father_node, node):
            if value == node.data:
                return father_node, node
            elif value < node.data:
                return find_node(node, node.left)
            else:
                return find_node(node, node.right)

        father_node, node = find_node(root, root)
        if node is self._root:
            if node.left is not None and node.right is not None:
                findMaxValueInLeftSubtree(node)
            elif node.left is None:
                self._root = node.right
            elif node.right is None:
                self._root = node.left
            else:
                self._root = None
        else:
            if node.left is not None and node.right is not None:
                findMaxValueInLeftSubtree(node)
            elif node.left is not None:
                if father_node.data > node.left.data:
                    father_node.left = node.left
                else:
                    father_node.right = node.left
            elif node.right is not None:
                if father_node.data > node.right.data:
                    father_node.left = node.right
                else:
                    father_node.right = node.right
            else:
                if father_node.data > node.data:
                    father_node.left = None
                else:
                    father_node.right = None
        self._size -= 1
        return value

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) is not None

    def height(self):

        def recurse(node):
            if node is None:
                return 0
            else:
                return 1 + max(recurse(node.left), recurse(node.right))

        h = recurse(self._root)
        if not self.isEmpty():
            h -= 1
        return h

    def isBlance(self):
        return self.height() < 2 * log(len(self) + 1, 2) - 1

    def clear(self):
        """Makes self become empty."""
        self._root = None
        self._size = 0

    def rebalance(self):
        """Rebalances the tree."""

        def rebulid(ly, left, right):
            if left <= right:
                mid = (left + right) // 2
                self.add(ly[mid])
                rebulid(ly, left, mid - 1)
                rebulid(ly, mid + 1, right)
        if not self.isBlance():
            lyst = list(self.inorder())
            self.clear()
            rebulid(lyst, 0, len(lyst) - 1)

    def predecessor(self, item):
        """Returns the smallest item that is larger than
                item, or None if there is no such item."""
        allLargerItems = list(filter(lambda x: x > item, self))
        if len(allLargerItems) > 0:
            return min(allLargerItems)
        else:
            return None

    def successor(self, item):
        """Returns the smallest item that is larger than
                        item, or None if there is no such item."""
        allSmallItems = list(filter(lambda x: x < item, self))
        if len(allSmallItems) > 0:
            return max(allSmallItems)

    def rangeFind(self, low, high):
        """Returns a list of the items in the tree, where
        low <= item <= high."""
        return list(filter(lambda item: item >= low and item <= high,
                           self.inorder()))


def main():
    tree = LinkedBST()
    print("Adding D B A C F E G")
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")
    print("\nString:\n" + str(tree))
    print("__iter__:", ",".join(tree.__iter__()))
    print("postorder:", ",".join(tree.postorder()))
    print("inorder:", ",".join(tree.inorder()))
    print("preorder:", ",".join(tree.preorder()))
    print("levelorder:", ",".join(tree.levelorder()))
    tree.remove("E")
    print("\nString:\n" + str(tree))
    print("height:", tree.height())
    print("Is balance?", tree.isBlance())

    print("Range find B-F:\n")
    print(tree.rangeFind("B", "F"))


if __name__ == "__main__":
    main()