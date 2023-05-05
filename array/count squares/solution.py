# O(n^2) time
# O(n) space - where n is the number of points

# check photo together with comments 
def countSquares(points):
    pointsSet = set()
    for point in points: # converts the count array into the set.
        pointsSet.add(pointToString(point)) 

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB: # skip same points
                continue

            midpoint = [(pointA[0]+pointB[0]) /2 ,(pointA[1]+pointB[1]) /2]

            # get the slope of the diagonal (using first two points)
            xDistanceFromMid = pointA[0] - midpoint[0]
            yDistanceFromMid = pointA[1] - midpoint[1]

            # the slope of the remaining diagnonal is -1 time that of original one (perpendicular)
            # thus y in x and x in y
            pointC = [midpoint[0] + yDistanceFromMid, midpoint[1] - xDistanceFromMid]
            pointD = [midpoint[0] - yDistanceFromMid, midpoint[1] + xDistanceFromMid]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                count += 1

    return count / 4  # every points will find a diagonal, so 4 points 4 same diagonals.

def pointToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0: # if both x and y are natural numbers.
        point = [int(coordinate) for coordinate in point]  # converting to integer if case there is a float 
    return ",".join([str(coordinate) for coordinate in point])