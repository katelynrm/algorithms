l = ["Hello", "World", "in", "a", "frame"]
# l = ["lets", "see", "if", "this", "actually", "works"]

def frame_print(array, frame_char):
    lengths = [len(i) for i in array]
    width = max(lengths)
    border = width + 4
    print(frame_char * border)
    for i in range(len(array)):
        print(frame_char, array[i].ljust(width), frame_char)

    print(frame_char * border)


frame_print(l, "*")

