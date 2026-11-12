class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
print("Popped:", s.pop())
print("Top:", s.peek())
print("Is Empty:", s.is_empty())
