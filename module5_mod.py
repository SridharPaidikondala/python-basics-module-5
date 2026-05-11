class NumberList:
    def __init__(self):
        self.numbers = []

    def initialize(self, n):
        self.numbers = [None] * n

    def insert(self, index, value):
        self.numbers[index] = value

    def search(self, x):
        for i, num in enumerate(self.numbers):
            if num == x:
                return i + 1  # 1-based index
        return -1
