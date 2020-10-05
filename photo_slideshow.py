import numpy as np

data = open("a_example.txt", "r")
image = []
x = 0

x = input()
print(x)

in = input()
print("Give me extra")
print(in)

# input
for i in data:
    if i != '':
        image.append(i.split(" "))
    image[x][-1] = image[x][-1][0:len(image[x][-1])-1]
    x = x + 1

number = chr(ord(image[0][0]))
del image[0]
similar = []

for i in image:
    tags1 = i[2:]
    term = tags1[0]
    del tags1[0]
    maxscore = 0
    for j in image:
        tags2 = j[2:]
        if i != j and term not in tags2:
            score = 0
            for k in tags1:
                if k in tags2:
                    score = score + 1

            if score > maxscore:
                maxscore = score
                similar = j

    print (i, " ", similar)
