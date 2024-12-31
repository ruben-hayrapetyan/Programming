import re
f = open("okay.txt", "r")
string = f.read()
dosplit = string.split('do()')
dontsplit = string.split('don\'t()')

goodlist = []
for i in range(len(dosplit)):
    if i % 2 == 0:
        goodlist.append(dosplit[i])
for j in range(len(dontsplit)):
    if i % 2 == 1:
        goodlist.append(dontsplit[j])
print(goodlist)
string = ''.join(goodlist)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
raw_matches = re.findall(pattern, string)

sum = 0
for i in raw_matches:
    thing = 1
    for j in i:
        thing *= int(j)
    sum += thing
print(sum)


# with open("problem3.txt", 'r') as f:
#     product = 0
#     hi = []
#     for line in f:
#         string = "do()" + line +"do()"
#         print(string)

#         res = re.split(r'don\'t\(\)(?:\\.|.)*?do\(\)', string)
#         print(res)

#         string = ''.join(res)

#         pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
#         raw_matches = re.findall(pattern, string)

#         print()
#         print()
#         print()
#         print(raw_matches)

#         for i in raw_matches:
#             thing = 1
#             for j in i:
#                 thing *= int(j)
#             if thing not in hi:
#                 hi.append(thing)
#         print(hi)
#     for i in hi:
#         product += i
#     print(product)


