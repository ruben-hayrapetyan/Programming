f = open("problem1.txt", "r")
string = f.read()
splitversion = string.split()
print(splitversion)
firstlist = []
secondlist = []
counter = 0
for i in splitversion:
    print("index = " + str(splitversion.index(i)))  
    if counter % 2 == 0:
        print("adding", i, "to first list")
        firstlist.append(i)
    else :
        print("adding", i, "to second list")
        secondlist.append(i)
    counter += 1

firstlist.sort()
secondlist.sort()

sum = 0
for i in firstlist:
    counter = 0
    for j in secondlist:
        if i == j:
            counter += 1
    sum += counter * int(i)

print(firstlist)
print()
print()
print()
print(secondlist)
print()
print()
print()
print(sum)