class ArrayListIterator(object):
    """Represents the list iterator for a array list."""

    def __init__(self, backingStore):
        """Set the initial state of the list iterator."""
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    def first(self):
        """Resets the cursor to the beginning of the backing store."""
        self._cursor = 0
        self._lastItemPos = -1

    def hasNext(self):
        """Returns True if the iterator has a next
        value or False otherwise."""
        return self._cursor < len(self._backingStore)

    def next(self):
        """Precondition: hasNext returns True.
        The list has not been modified except by
        this iterator's mutators.
        Returns the current value and advances the cursor."""
        if not self.hasNext():
            raise ValueError("No next value in list iterator.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def last(self):
        """Moves the cursor to the end of the backing store."""
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasPrevious(self):
        """Return True if the iterator has a previous value or False otherwise."""
        return self._cursor > 0

    def previous(self):
        """Precondition: hasPrevious returns True.
        The list has not been modified except by
        this iterator's mutators.
        Returns the current value and moves the cursor to the previous value."""
        if not self.hasPrevious():
            raise ValueError("No previous value in list iterator.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]

    def replace(self, value):
        """Precondition: the current position is defined.
        The list has not been modified except by this iterator's mutators."""
        if self._lastItemPos == -1:
            raise AttributeError("The current position is not defined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        self._backingStore[self._lastItemPos] = value
        self._lastItemPos = -1

    def insert(self, value):
        """Precondition: The list has not been modified except by this iterator's mutators."""
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        # cursor not defined, so add value in the end of list.
        if self._lastItemPos == -1:
            self._backingStore.add(value)
        else:
            self._backingStore.insert(self._lastItemPos, value)
        self._lastItemPos = -1
        self._modCount += 1

    def remove(self):
        """Precondition: the current position is defined.
        The list has not been modified except by this iterator's mutators."""
        if self._lastItemPos == -1:
            raise AttributeError("The current position is not defined.")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("List has been modified illegally.")
        value = self._backingStore.pop(self._lastItemPos)
        # If the value removed was obtained via next move cursor back.
        if self._lastItemPos < self._cursor:
            self._cursor -= 1
        self._modCount += 1
        self._lastItemPos = -1