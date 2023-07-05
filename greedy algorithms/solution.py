def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesleft = len(queries)-(idx+1)
        totalWaitingTime += duration * queriesleft

    return totalWaitingTime