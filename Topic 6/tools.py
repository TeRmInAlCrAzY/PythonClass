def printHeader(title):
    printLine(len(title))
    print("~" * 3, " " * 4, title, " " * 4, "~" * 3)
    printLine(len(title))

def printLine(length):
    numprints = length + 4 + 4 + 3 + 3 + 4
    print("~" * numprints)