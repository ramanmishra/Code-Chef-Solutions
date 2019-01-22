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
    s = myStack()
    operand = ""
    exp = input()
    for j in exp:
        if j.isalpha():
            operand += j
        else:
            p = ""
            if j == ")":
                while p != "(":
                    p = s.pop()
                    if p == "+" or p == "-" or p == "*" or p == "/" or p == "^":
                        operand += p
            else:
                s.push(j)
    print(operand)