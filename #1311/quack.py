class Quack:
    def __init__(self):
        self.leftStack = []
        self.middleStack = []
        self.rightStack = []

    def push(self, x):
        self.leftStack.append(x)

    def pop(self):
        if not self.leftStack:
            while self.middleStack:
                self.leftStack.append(self.middleStack.pop())
        if self.leftStack:
            return self.leftStack.pop()
        return None

    def pull(self):
        if not self.rightStack:
            while self.middleStack:
                self.rightStack.append(self.middleStack.pop())
        if self.rightStack:
            return self.rightStack.pop()
        return None

if __name__ == '__main__':
    quack = Quack()
    quack.push(1)
    quack.push(2)
    quack.push(3)
    print(quack.pop()) # Outputs 1
    quack.push(4)
    quack.push(5)
    print(quack.pull()) # Outputs 5
