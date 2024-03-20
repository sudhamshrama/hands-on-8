class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, item):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]


# Example usage:
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print("Top of the stack:", stack.peek())
print("Popped item:", stack.pop())
print("Top of the stack after popping:", stack.peek())
