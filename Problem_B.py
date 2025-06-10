# read input
num_v, num_e = map(int, input().split( ))

p = [0] * num_v
rank = [0] * num_v

# make Set
def make(i):
    p[i] = i
    rank[i] = 0

for i in range(num_v):
    make(i)

# make edge
edges = []
for _ in range(num_e):
    s, t, w = map(int, input().split( ))
    edges.append((s, t, w))

# find Set
def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]

# link Set
def link(s, t):
    if rank[s] > rank[t]:
        p[t] = s
    else:
        p[s] = t
        if rank[t] == rank[s]:
            rank[t] += 1

# unite set
def unite(s, t):
    link(find(s), find(t))

# get weight
def get_weight(edge):
    return edge[2]

# kruskal algorithm
def kruskal():
    mst_weight = 0
    edges.sort(key=get_weight) # sort edges in ascending order based on weights
    for s, t, w in edges:
        if find(s) != find(t):
            unite(s, t)
            mst_weight += w
    print(mst_weight)

kruskal()