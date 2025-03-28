def dfs(graph,start,goal,path=[]):
    path.append(start)
    if start==goal :
        return path
    for neighbor in graph[start]:
        result=dfs(graph,neighbor,goal,path)
        if result:
            return result
    path.pop()
    return None
graph={
    0:[1,2],
    1:[3,4],
    2:[5,6],
    3:[7],
    4:[7],
    5:[7],
    6:[7],
    7:[]
}
print(dfs(graph,0,7) or "No path found")
