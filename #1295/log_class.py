class Log:
    def __init__(self, n):
        self.n = n
        self.log = []
        self.curr_index = 0

    def record(self, order_id):
        if len(self.log) < self.n:
            self.log.append(order_id)
        else:
            self.log[self.curr_index] = order_id
            self.curr_index = (self.curr_index + 1) % self.n

    def get_last(self, i):
        return self.log[(self.curr_index - i + self.n) % self.n]

log = Log(5)
log.record(1)
log.record(2)
log.record(3)
log.record(4)
log.record(5)

# Overwrite the oldest entry
log.record(6)

if __name__ == '__main__':
    print(log.get_last(1)) # Output 6
    print(log.get_last(2)) # Output 5
    print(log.get_last(3)) # Output 4
    print(log.get_last(4)) # Output 3
    print(log.get_last(5)) # Output 2
