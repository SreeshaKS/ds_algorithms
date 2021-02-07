def dfs(curr, adj,visited, g_from, g_to, path):
    print("visiting children of",curr)
    for node in adj[curr]:
        if node not in path:
            if visited[node] and node not in path:
                return path+[node]
            
            visited[node] = True
            return dfs(node, adj, visited, g_from, g_to, path+[node])
    return []
    

def nodeDistance(g_nodes, g_from, g_to):
    # Write your code here
    adj = {}
    visited = {}
    dist = []
    for n in range(g_nodes):
        adj[n+1] = []
        visited[n+1] = False
    
    for idx, node in enumerate(g_from):
        adj[node].append(g_to[idx])
        adj[g_to[idx]].append(node)
    print(adj)
    path = []
    start = g_from[0]
    print(start)
    print("visiting children of",start)
    for node in adj[start]:
        visited[node] = True
        print(node)
        p = dfs(node, adj, visited, g_from, g_to, path+[node])
        return p

print(nodeDistance(6,[1,2,1,3,1,2],[2,3,3,5,4,6]))