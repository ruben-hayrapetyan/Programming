def evaluate(individual):
    bad = 0
    greater = None
    prev_start = individual[0]
    for j in range(1, len(individual)):
        current = int(individual[j])
        prev = int(prev_start)
        if greater is None:
            if current > prev:
                greater = True
            elif current < prev:
                greater = False
        elif (greater and current < prev) or (not greater and current > prev):
            bad += 1
        if abs(current - prev) > 3:
            bad += 1
        if current == prev:
            bad += 1
        prev_start = current
    return bad < 1

f = open("problem2.txt", "r")
string = f.read()
splitversion = string.split('\n')
print(splitversion)
count = 0
for level in splitversion:
    individual = level.split()
    if not individual:
        continue
    print(individual)
    if evaluate(individual) == True:
        print("good:", individual)
        count += 1
    else:
        print("INDIVIDUAL", individual)
        for removeelement in range(len(individual)):
            copything = individual[:removeelement] + individual[removeelement+1:]
            if evaluate(copything) == True:
                print("good inside:", copything)
                count += 1
                break

print(count)
