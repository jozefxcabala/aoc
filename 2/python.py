f = open("input.txt", "r")

depth = 0
horizonatl = 0
aim = 0

for i in f:
    if(i.split()[0] == "down"):
        aim += int(i.split()[1])
    elif(i.split()[0] == "forward"):
        horizonatl += int(i.split()[1])
        depth += aim*int(i.split()[1])
    elif(i.split()[0] == "up"):
        aim -= int(i.split()[1])

print("depth: ", depth)
print("horizontal: ", horizonatl)
print("aim: ", aim)
print("*: ", horizonatl * depth)


