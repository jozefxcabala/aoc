from typing import Counter
import copy

file = open("6\\input.txt", "r")
initialState = dict(Counter(file.read().split(",")))
newState = copy.deepcopy(initialState)

day = 0
newFish = 0
while(day != 256):
    for key in initialState:
        if(int(key) != 0):
            if str(int(key) - 1) in newState.keys():
                newState[str(int(key) - 1)] += initialState[key]
            else:
                newState[str(int(key) - 1)] = 0
                newState[str(int(key) - 1)] += initialState[key]
            
            newState[key] -= initialState[key]
        else:
            if "6" in newState.keys():
                newState["6"] += initialState[key]    
            else:
                newState["6"] = 0
                newState["6"] += initialState[key] 

            newFish += initialState[key] 
            newState[key] -= initialState[key]

    
        if(newFish > 0):
            if "8" in initialState.keys():
                newState["8"] += newFish   
            else:
                newState["8"] = 0
                newState["8"] += newFish

        newFish = 0

    day += 1
    initialState = copy.deepcopy(newState)

sum = 0
for key in initialState:
    sum += int(initialState[key])

print(sum)



    