#Andrew Larson
#​CSCI 102 – Section A
#Week 12 - Part B
def PrintOutput(x):
    x = str(x)
    print("OUTPUT", x)
def LoadFile(x):
    lines = []
    file_txt = open(x, "a")
    for line in file_txt:
        lines.append(line)
    print("OUTPUT", lines)
def UpdateString(x,y,z):
    word = list(x)
    word[z] = y
    word = ''.join(word)
    print('OUTPUT', word)
def FindWordCount(a,b):
    sum_words = 0
    for i in a:
        if i == b:
            sum_words = sum_words+1
    return sum_words
