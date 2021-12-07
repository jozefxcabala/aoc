file = open("7\\input.txt", "r")
positions = list(map(int, file.read().split(",")))

minFuel = 0
fuel = 0
step = 0

for i in range(max(positions)):
    for j in range(len(positions)):     
        fuel += sum(range(1, abs(i - positions[j]) + 1))
        step = 0

    if(i == 0):
        minFuel = fuel
    elif(fuel < minFuel):
        minFuel = fuel

    fuel = 0

print(minFuel)