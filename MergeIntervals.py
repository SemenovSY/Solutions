def merge(intervals):
    intervals.sort()

    new_intervals = []
    new_intervals.append(intervals[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= new_intervals[len(new_intervals)-1][1]:
            if intervals[i][1] < new_intervals[len(new_intervals)-1][1]:
                new_intervals[len(new_intervals)-1][1] = intervals[i][1]              
        else:
            new_intervals.append(intervals[i])
        
    return new_intervals

print(merge([[1,3],[2,6],[8,10],[15,18]]))
