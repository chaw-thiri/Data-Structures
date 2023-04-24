# both solutions have same space and time complexity 
# time = O(n*2)
# space = O (n)
# find all the points that shares the same x value
# find the edge that have same y value

def minimumAreaRectangle(points):
    pointSet = createPointSet(points)
    minAreaFound = float("inf") 

    for currentIdx, p2 in enumerate(points):
        p2x, p2y = p2 # ???
        for previousIdx in range(currentIdx):
            p1x, p1y = points[previousIdx]
            pointsShareValue = ( p1x== p2x ) or ( p1y==p2y )

            if pointsShareValue:
                continue

            # if p1x,p1y,p2x,p2y exist >> we found a rectangle
            point1OnOppositeDiagonalExist = convertPointToString(p1x,p2y) in pointSet
            point2OnOppositeDiagonalExist = convertPointToString(p2x, p1y) in pointSet
            oppositeDiagonalExists = point1OnOppositeDiagonalExist and point2OnOppositeDiagonalExist  # ???

            if oppositeDiagonalExists:
                currentArea = abs(p2x-p1x) * abs(p2y-p1y)
                minAreaFound = min(minAreaFound, currentArea)

    return minAreaFound if  minAreaFound != float("inf") else 0


def createPointSet(points):
    pointSet = set() # empty set

    for point in points:
        x,y = point
        pointString = convertPointToString(x,y)
        pointSet.add(pointString)
    
    return pointSet

def convertPointToString(x,y ):
    return str(x) + ":" + str(y)


points= [
    [1, 5],
    [5, 1],
    [4, 2],
    [2, 4],
    [2, 2],
    [1, 2],
    [4, 5],
    [2, 5],
    [-1, -2]]
print(minimumAreaRectangle(points))