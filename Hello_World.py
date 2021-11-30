print("Hello World")


def hello_world():
    print("Hello World")


def hello_world_2(word):
    if word == "World":
        print("Hello " + word)
    else:
        print("Goodbye " + word)


if __name__ == "__main__":
    hello_world()
    hello_world_2("Test")
    hello_world_2("World")
