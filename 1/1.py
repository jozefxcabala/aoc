f = open("input.txt", "r")
depth = 0
numberOfIncrease = 0

for x in f:
    if(int(x) > depth):
        numberOfIncrease += 1
    depth = int(x)

numberOfIncrease -= 1

print("Number of increase: " + str(numberOfIncrease))
    

f = open("input.txt", "r")
array = []
sucty = []
pocitadlo = 0
medziSucet = 0
depth = 0
numberOfIncrease = 0

for x in f:
    array.append(int(x))

for i in range(len(array)):
    if(i == (len(array)-2)):
        break
    sucty.append(array[i]+array[i+1]+array[i+2])

for i in range(len(sucty)):
    if(sucty[i] > depth):
        numberOfIncrease += 1
    depth = sucty[i]

numberOfIncrease -= 1

print("Number of increase: " + str(numberOfIncrease))
