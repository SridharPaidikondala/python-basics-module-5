from module5_mod import NumberList


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
