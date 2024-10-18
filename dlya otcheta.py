# мы сами ввели все значения
graph = [[], [2, 3], [1, 3], [1, 2], [5], [4]]
visited = [0] * 6

def dfs(now, gragh, visited, marker):
  visited[now] = marker
  for neigh in gragh[now]:
    if visited[neigh] == 0:
      dfs(neigh, gragh, visited, marker)

marker = 1
for i in range(1, 6):
  if visited[i] == 0:
    dfs(i, graph, visited, marker)
    marker += 1

print(max(visited))

# пользователь вводит значения
n = int(input("введите кол-во вершин: "))
m = int(input("введите кол-во ребер: "))

g = [[] for x in range(n + 1)]

visited = [0 for x in range(n + 1)]

for i in range(m):
    first = int(input())
    second = int(input())
    g[first].append(second)
    g[second].append(first)

def dfs(now, g, visited, marker):
    visited[now] = marker
    for neigh in g[now]:
        if 0 == visited[neigh]:
            dfs(neigh, g, visited, marker)

marker = 1
for i in range(1, n + 1):
    if 0 == visited[i]:
        dfs(i, g, visited, marker)
        marker += 1

print(max(visited))