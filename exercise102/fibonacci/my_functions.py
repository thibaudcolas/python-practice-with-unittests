from collections import deque


def fibonacci(upto):
    if upto == 0:
        return 0
    if upto == 1:
        return 1

    return fibonacci(upto - 1) + fibonacci(upto - 2)


def ask_how_many():
    user_input = input("How many?")
    try:
        int_input = int(user_input)
    except ValueError:
        raise ValueError("Value is not an integer")

    if int_input < 0:
        raise ValueError("Value is not a positive integer")

    return int_input


def main():
    choice = ask_how_many()
    print(fibonacci(choice))


if __name__ == "__main__":
    main()
