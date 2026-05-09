# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

_SENTINEL = object()

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._it = iterator
        self._buf = self._it.next() if self._it.hasNext() else _SENTINEL
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._buf
        

    def next(self):
        """
        :rtype: int
        """
        v = self._buf
        self._buf = self._it.next() if self._it.hasNext() else _SENTINEL
        if v is _SENTINEL:
            raise StopIteration()
        return v
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._buf is not _SENTINEL
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].