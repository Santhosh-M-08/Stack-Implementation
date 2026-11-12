class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            value = self.stack[self.top]
            self.top -= 1
            return value

    def peek(self):
        if self.top == -1:
            return "Stack is Empty"
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def display(self):
        print(self.stack[:self.top + 1])


s = Stack(5)

s.push(10)
s.push(20)
s.push(30)

s.display()
print("Popped:", s.pop())
print("Top:", s.peek())
print("Is Empty:", s.is_empty())
