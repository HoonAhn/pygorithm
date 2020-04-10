def dfs(graph, start):
    visit = set()
    stack = [start]

    while stack:
        v = (stack.pop())

        if v in visit:
            continue
        
        visit.add(v)

        for n in graph[v]:
            if n not in visit:
                stack.append(n)
    return visit

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
    "H": []
}

print(dfs(G, "H"))