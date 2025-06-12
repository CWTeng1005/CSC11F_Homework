import sys
sys.setrecursionlimit(1 << 25)

n, q = map(int, input().split())
parent = list(range(n))
diff_weight = [0] * n  # diff_weight[x] = a[x] - a[parent[x]]

def find(x):
    if parent[x] != x:
        orig = parent[x]
        parent[x] = find(parent[x])
        diff_weight[x] += diff_weight[orig]
    return parent[x]

def unite(x, y, w):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    parent[rx] = ry
    diff_weight[rx] = diff_weight[y] - diff_weight[x] + w

def diff(x, y):
    if find(x) != find(y):
        print("?")
    else:
        print(-(diff_weight[y] - diff_weight[x]))

for _ in range(q):
    line = list(map(int, input().split()))
    if line[0] == 0:
        _, x, y, z = line
        unite(x, y, z)
    else:
        _, x, y = line
        diff(x, y)