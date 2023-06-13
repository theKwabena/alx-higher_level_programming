#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of list arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argument is.")
    elif count == 1:
        print("1 argument is:")
    else:
        print("{} arguments are:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
