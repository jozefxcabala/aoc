import math
from collections import Counter

file = open("5\\input.txt", "r")
points = [[list(map(int,p[0].split(','))), list(map(int,p[1].split(',')))] for p in [l.split(' -> ') for l in file.read().split("\n")]]

class Point:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
    
    def __str__(self):
        return f"x={self.x0} y={self.y0}"

class Line:
    def __init__(self, point0, point1):
        self.point0 = point0
        self.point1 = point1

        #part1
        if((self.point0.x0 == self.point1.x0) or (self.point0.y0 == self.point1.y0)):
            self.pointOnLine = self.getPointsOnLine()
        else:
            self.pointOnLine = []

    def getPointsOnLine(self):
        pointsOnLine = []
        startX = self.point0.x0  if self.point0.x0 < self.point1.x0 else self.point1.x0
        endX = self.point1.x0  if self.point0.x0 < self.point1.x0 else self.point0.x0
        startY = self.point0.y0  if self.point0.y0 < self.point1.y0 else self.point1.y0
        endY = self.point1.y0  if self.point0.y0 < self.point1.y0 else self.point0.y0

        for i in range(startX, endX + 1):
            for j in range(startY, endY + 1):
                if(self.pointIsOnLine(i, j)):
                    pointsOnLine.append(Point(i, j))
        
        return pointsOnLine

    def pointIsOnLine(self, x0, y0):  
        AB = math.sqrt(pow(self.point1.x0 - self.point0.x0, 2) + pow(self.point1.y0 - self.point0.y0, 2))
        AP = math.sqrt(pow(self.point1.x0 - x0, 2) + pow(self.point1.y0 - y0, 2))
        PB = math.sqrt(pow(x0 - self.point0.x0, 2) + pow(y0 - self.point0.y0, 2))
        if(AB == AP + PB):
            return True
        else:
            return False
    
    def __str__(self):
        line = f"line: point0 {str(self.point0)} point1 {str(self.point1)}"
        points = ""
        for i in range(len(self.pointOnLine)):
            points += f"point{str(i)}" + " " + str(self.pointOnLine[i]) + "\n"
        return line + "\n" + points

lines = []
for i in range(len(points)):
    lines.append(Line(Point(points[i][0][0], points[i][0][1]), Point(points[i][1][0], points[i][1][1])))

pointsOfLines = []

for i in range(len(lines)):
    for k in range(len(lines[i].pointOnLine)):
        pointsOfLines.append(str(lines[i].pointOnLine[k]))

numberOccurencesOfEachPoints = dict(Counter(pointsOfLines))
sum = 0

for key in numberOccurencesOfEachPoints:
    if(numberOccurencesOfEachPoints[key] > 1):
        sum += 1

print(sum)
