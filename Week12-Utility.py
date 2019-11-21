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
def ScoreFinder(x,y,z):
    score = 0
    if z in x:
        index = x.index(z)
        score = y[index]
        print('OUTPUT', z, 'got a score of', score)
    else:
        print('OUTPUT player not found')
def Union(x,y):
    final_list = x+y
    return final_list
def Intersection(x,y):
    shared_list = []
    for i in x:
        if i in y:
            shared_list.append(i)
    return shared_list
        
