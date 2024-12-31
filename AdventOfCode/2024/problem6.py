def mark (guardmap, face): #face = 0 (forward) face = 1 (backwards) face = 2 (right) face = 3 (left)
    for line in guardmap:        
        print(line)
    print("FACE:", face)
    print()
    print()
    print()
    widthindex = -1
    heightindex = -1
    totalheight = len(guardmap)
    totalwidth = len(guardmap[0])
    for i in range(len(guardmap)):
        for j in range(len(guardmap[0])):
            if guardmap[j][i] == '^':
                widthindex = j
                heightindex = i

    if (face == 0 and heightindex-1 < 0):
        print("IN FIRST CORNER CASE")
        for line in guardmap:        
            print(line)
        return
    elif (face == 1 and heightindex+1 > totalheight):
        print("IN SECOND CORNER CASE")
        for line in guardmap:        
            print(line)
        return
    elif (face == 2 and widthindex+1 > totalwidth):
        print("IN THIRD CORNER CASE")
        for line in guardmap:        
            print(line)
        return
    elif (face == 3 and widthindex-1 < 0):
        print("IN FOURTH CORNER CASE")
        for line in guardmap:        
            print(line)
        return
    
    if (guardmap[widthindex][heightindex-1] == '#'):
        if (face == 0):
            mark(guardmap, 2)
        elif (face == 1):
            mark(guardmap, 3)
        elif (face == 2):
            mark(guardmap, 1)
        elif (face == 3):
            mark(guardmap, 0)
    
    if (face == 0):
        guardmap[widthindex][heightindex-1] = '^'
    elif (face == 1):
        guardmap[widthindex][heightindex+1] = '^'
    elif (face == 2):
        guardmap[widthindex+1][heightindex] = '^'
    elif (face == 3):
        guardmap[widthindex-1][heightindex] = '^'
    
    guardmap[widthindex][heightindex] = 'X'
    mark(guardmap, face)        
        
        

f = open("problem6.txt", "r")
string = f.read()
stringsplit = string.split('\n')
guardmap = []
for line in stringsplit:
    minilist = []
    for char in range(len(line)):
        minilist.append(line[char])
    guardmap.append(minilist)
    #print(minilist)

mark(guardmap, 0)

print(guardmap)