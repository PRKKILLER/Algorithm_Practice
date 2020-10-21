
"""  
A vehicle assignment is an array with 4 entries:
vehicle id
driver id
start timestamp (inclusive)
end timestamp (exclusive)

Given some vehicle assignments and a driver id, returns the duration,
in 'time units', for which that vehicle was assigned to a driver
"""

def solution(assignments, id):
    data = list(filter(lambda x: x[0] == id, assignments))
    data = map(lambda x: [x[2], x[3]], data)

    intervals = sorted(data, key=lambda x: x[0])
    res = []

    start, end = intervals[0][0], intervals[0][1]

    for pair in intervals[1:]:
        if pair[0] <= end:
            end = max(end, pair[1])
        else:
            res.append([start, end])
            start, end = pair[0], pair[1]
    
    res.append([start, end])

    total = 0
    for pair in res:
        total += (pair[1] - pair[0])

    return total

assignments = [
    [100,30,660000,660200],
    [100,31,660000,660200],
    [100,32,700000,700200],
    [200,33,245245,654636]
]

v_id = 100

print(solution(assignments, v_id))
