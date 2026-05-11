class MyQueue:

    def __init__(self):
        self.s1 = []  # for push
        self.s2 = []  # for pop/peek

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self._shift()
        return self.s2.pop()

    def peek(self):
        self._shift()
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2
    
    def _shift(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())