def say_hello():
    print('hello')


say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')


show_tree()

print(show_tree)  # <function show_tree at 0x000001A7C00BEA60> (location in memory)
