# 너비 우선 탐색
# 그래프 표현 (예시)

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append (node)
    queue. append (node)

    while queue:
        s = queue. pop (0)
        print (s)

        for neighbour in graph [s]:
            if neighbour not in visited:
                visited.append (neighbour)
                queue. append (neighbour)
                
bfs(visited, graph, 'A')