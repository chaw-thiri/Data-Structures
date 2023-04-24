# time = O (n^2)
# space = O(n)
def minimumAreaRectangle(points):
    columns = initializeColumns(points)
    minAreaRound = float("inf")
    edgesParalletToYAxis = {}    # 1 : [2,5] , 2 : [2,4,5], 4 : [5,2], 5 :[1], -1 : [-2] 
 

    sortedCol = sorted(columns.keys())  # -1 : [-2], 1 : [2,5] , 2 : [2,4,5], 4 : [5,2], 5 :[1],
    for x in sortedCol:
        yValuesInCurrentColumns = columns[x]
        yValuesInCurrentColumns.sort() # 4 : [5,2] >>> 4:[2:5]

        for currentIdx, y2 in enumerate(yValuesInCurrentColumns):
            for previousIdx in range(currentIdx): 
                y1 = yValuesInCurrentColumns[previousIdx]
                pointString = str(y1) + ":" + str(y2)
    
                if pointString in edgesParalletToYAxis:
                    currentArea = (x-edgesParalletToYAxis[pointString]) * (y2-y1)
                    minAreaRound = min(minAreaRound,currentArea)
    
                edgesParalletToYAxis[pointString] = x

    return minAreaRound if minAreaRound != float("inf") else 0

def initializeColumns(points):
    columns = {}  # [2,5] is at the column 1 
    # [2,5] : 1 , [2:4] : 2, 
    # [2,5] : 2 overwrite 

    for point in points:
        x,y = point 
        if x not in columns:
            columns[x] = [] # ????

        columns[x].append(y)

    return columns