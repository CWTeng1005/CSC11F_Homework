# read n, q
n, q = map(int, input().split( ))

p = [0] * n
rank = [0] * n

# makeSet
def make(i):
    p[i] = i
    rank[i] = 0

for i in range(n):
    make(i)

# findSet
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

# link 2 sets
def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[y] == rank[x]:
            rank[y] = rank[y]+1

# unite
def unite(x,y):
    link(find(x), find(y))

# same
def same(x,y):
    if find(x) == find(y):
        print("1")
    else:
        print("0")

# read queries
for _ in range(q):
    com, x, y = map(int, input().split())
    # queries: 0: unite; 1: define same
    if com == 0:
        unite(x, y)
    else:
        same(x, y)