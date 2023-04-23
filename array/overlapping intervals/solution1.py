# time = O(nlogn) (sorting) | space = O(n)
def mergeOverlappingIntervals(intervals):
    # sort the array first 
    sorted_interval = sorted(intervals, key = lambda x: x[0]) # sorted according to the start interval

    # find the merge
    merged_interval =[]
    current_interval = sorted_interval[0]
    merged_interval.append(current_interval)

    
    for nextInterval in sorted_interval:
        # for clarity name the start and end of the current and next varaible seperately 
        _, currentIntervalEnd = current_interval
        next_interval_start, next_interval_end = nextInterval
        if currentIntervalEnd >= next_interval_start: # without equal, start and end duplicates will be skipped.
            current_interval[1]= max(currentIntervalEnd,next_interval_end)
        else:
            current_interval = nextInterval # modify current interval for next comparison
            merged_interval.append(current_interval)
    return merged_interval
