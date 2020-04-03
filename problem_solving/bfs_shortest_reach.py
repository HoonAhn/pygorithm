# https://www.hackerrank.com/challenges/bfsshortreach/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# solved 20/04/03

# n: the integer number of nodes
# m: the integer number of edges
# edges: a 2D array of start and end nodes for edges
# s: the node to start traversals from

# 1. make a graph from the inputs
# 2. make a queue and a checklist, start searching from s
# 3. starting from s, try to visit from the lowest node

def bfs(n, m, edges, s):
    g = [[] for _ in range(n+1)]
    check = [-1 for _ in range(n+1)]
    q = []
    q.append(s)
    check[s] = 0
    for i in edges:
        if g[i[0]].count(i[1]) == 0:
            g[i[0]].append(i[1])
        if g[i[1]].count(i[0]) == 0:
            g[i[1]].append(i[0])
    print(g)
    while len(q) > 0:
        x = q[0]
        q.pop(0)
        print("visit ",x)
        for i in range(len(g[x])):
            y = g[x][i]
            if (check[y] == -1):
                print("**found ",y)
                check[y] = check[x]+6
                q.append(y)
    check.pop(check.index(0))
    return(check[1:])
       
print(bfs(5,3,[[1,2],[1,3],[3,5],[2,4]],1))