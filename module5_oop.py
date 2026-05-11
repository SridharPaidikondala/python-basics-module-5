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


def main():
    n = int(input("Enter a positive integer N: "))

    number_list = NumberList()
    number_list.initialize(n)

    for i in range(n):
        val = int(input(f"Enter number {i + 1}: "))
        number_list.insert(i, val)

    x = int(input("Enter X to search for: "))
    result = number_list.search(x)
    print(result)


if __name__ == "__main__":
    main()
