# https://www.hackerrank.com/challenges/bfsshortreach/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# started 20/03/31

# n: the integer number of nodes
# m: the integer number of edges
# edges: a 2D array of start and end nodes for edges
# s: the node to start traversals from

# 1. make a graph from the inputs
# 2. make a queue and a checklist, start searching from s
# 3. 
def bfs(n, m, edges, s):
    g = [[0]*n]*n
    check = [False] * (n+1)
    q = []
    q.append(s)
    check[s] = True
    for i in edges:
        g[i[0]-1] = i[1]
    print(g)
    while len(q) > 0 {
        x = q[0]
        q.pop(0)
        print("%d " % x)
        for i in range(len(g[x-1])):

    }
       

