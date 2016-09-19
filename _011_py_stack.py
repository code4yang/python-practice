class Stack:
    def __init__(self):
        self._elements = []
        self._size = 0
        self._head = -1
        self._end = -1

    def pop(self):
        return self._elements.pop()

    def push(self, elem):
        return self._elements.append(elem)

    def clear(self):
        self._elements = []
        return

    def get(self):
        return self._elements[len(self._elements)]

    def is_full(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def show(self):
        pass

