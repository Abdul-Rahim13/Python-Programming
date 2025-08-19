Graph = {
    'A': {},
    'B': {'E':2},
    'C': {'F':1},
    'D': {'B':3, 'G':8},
    'E': {'G':2},
    'F': {'E':0, 'G':4},
    'S': {'A':3, 'C':2, 'D':2}
}

def BFS (start, goal):
    cost = 0
    path = []
    visited = set()
    queue = ([(cost, start)])

    while queue:
        cost, current = queue.pop()
        if current == goal:
            path.append(current)
            return cost, path
        if current not in visited:
            path.append(current)
            visited.add(current)
            
            for x,y in reversed(Graph.get(current,{}).items()):
                queue.append((y+cost, x))
    return float('inf'), None

print(BFS('S','G'))
