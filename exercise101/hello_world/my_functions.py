def hello(name):
    print("Hello, {}".format(name))


def ask_for_name():
    return input("What is your name?")


def main():
    txt = ask_for_name()
    hello(txt)


if __name__ == "__main__":
    main()
