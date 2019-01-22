class myStack:
    def __init__(self):
        self.container = []

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        return self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Empty!")
        return self.container[len(self.container) - 1]

    def size(self):
        return len(self.container)

    def show(self):
        return self.container


t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    while n != 0:
        if n >= 100:
            n -= 100
            c += 1
        elif n >= 50:
            n -= 50
            c += 1
        elif n >= 10:
            n -= 10
            c += 1
        elif n >= 5:
            n -= 5
            c += 1
        elif n >= 2:
            n -= 2
            c += 1
        elif n >= 1:
            n -= 1
            c += 1
    print(c)