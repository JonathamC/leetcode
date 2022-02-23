def merge(intervals): 
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]: 
        # if overlapped 
        if start <= output[-1][1]: 
            output[-1][1] = max(end, output[-1][1])
        else: 
            output.append([start, end])
    return output





intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
print(merge(intervals))