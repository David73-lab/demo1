def fibonach(sequenceLen):
    num = 0
    nextnum = 1
    fibolist = [num, nextnum]
    for i in range(sequenceLen):
        fibolist += [(num + nextnum)]
        helper = num
        num = nextnum
        nextnum = helper + nextnum
        yield fibolist[len(fibolist) - 1]


gen = fibonach(9)
print(next(gen))


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
