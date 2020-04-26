class _NodeStack:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self._top = None    
        self._size = 0

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self._top.data
    
    def push(self, element):
        new_node = _NodeStack(element)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self):
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def print_stack(self):
        pointer = self._top
        while pointer:
            print(pointer.data)
            pointer = pointer.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Before pop:")
    stack.print_stack()
    print("Top ->", stack.peek())
    print("Length -> ", len(stack))
    stack.pop()
    print("After pop")
    stack.print_stack()
    print("Top ->", stack.peek())
    print("Length -> ", len(stack))

    