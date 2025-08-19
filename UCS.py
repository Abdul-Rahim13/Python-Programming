import heapq

Graph = {
    'S':{'A':3,'D':2,'C':2},
    'A':{},
    'D':{'B':3,'G':8},
    'C':{'F':3},
    'B':{'E':2},
    'G':{},
    'F':{'E':0, 'G':4},
    'E':{'G':2}
}

def UCS (start, goal):
    cost = 0
    path = []
    visited = set()
    queue = [(cost, start, path)]

    while queue:
        cost, current, path = heapq.heappop(queue)
        if current == goal:
            path.append(current)
            return cost, path
        if current not in visited:
            visited.add(current)
            path = path+[current]

            for x, y in Graph.get(current, {}).items():
                heapq.heappush(queue, (y+cost, x, path))

    return float('inf'), None

print(UCS('S','G'))