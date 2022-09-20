def hello():
    print("Hello Broski")


def pack(item1, item2, item3):
    return [item1, item2, item3]


def eat_lunch(*lunch):
    x = 0
    for i in lunch:
        if x == 0:
            print("First i eat", i)
        else:
            print("Next i eat", i)
        x += 1
    print("My lunch is gone")


hello()
pack("1", "2", "3")
eat_lunch("Ham", "Pizza", "Cheese", "Roll Up")
