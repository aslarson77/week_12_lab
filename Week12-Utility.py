#Andrew Larson
#​CSCI 102 – Section A
#Week 12 - Part B
def PrintOutput(x):
    x = str(x)
    print("OUTPUT", x)
def LoadFile(x):
    lines = []
    file_txt = open(x, "r")
    for line in file_txt:
        lines.append(line)
    print("OUTPUT", lines)
def UpdateString(x,y,z):
    word = list(x)
    word[z] = y
    word = ''.join(word)
    print('OUTPUT', word)

