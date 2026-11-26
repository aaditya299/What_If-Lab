graph = {
    "motivation": ["study_hours", "exam_score"],
    "study_hours": ["exam_score"],
    "exam_score": []
}
cyclic_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}
invalid_graph = {
    "A": ["C"],
    "B": []
}

def has_path(graph,start,target):
    if start==target:
        return True
    for child in graph[start]:
        if has_path(graph,child,target):
            return True
    return False

def has_cycle(graph):
    visited=set()
    path=set()
    def dfs(node):
        if node in path:
            return True
        if node in visited:
            return False 
        visited.add(node)
        path.add(node)
        for child in graph[node]:
            if dfs(child):
                return True
        path.remove(node)
        return False
    for node in graph:
        if dfs(node):
            return True
    return False 

def validate_graph(graph):
    for node in graph:
        for child in graph[node]:
            if child not in graph:
                return False
    if has_cycle(graph):
        return False
    return True

def topological_sort(graph):
    indegree={node:0 for node in graph}
    for node in graph:
        for child in graph[node]:
            indegree[child]+=1
    queue=[node for node,deg in indegree.items() if deg==0]
    order=[]
    while queue:
        node=queue.pop(0)
        order.append(node)
        for child in graph[node]:
            indegree[child]-=1
            if indegree[child]==0:
                queue.append(child)
    if len(order)==len(graph):
        return order
    else:
        return None
    

print(has_path(graph, "motivation", "exam_score"))
print(has_path(graph, "motivation", "study_hours"))
print(has_path(graph, "study_hours", "motivation"))
print(has_path(graph, "exam_score", "motivation"))

print(has_cycle(graph))        
print(has_cycle(cyclic_graph)) 

print(validate_graph(graph))          
print(validate_graph(invalid_graph))  
print(validate_graph(cyclic_graph))  

print(topological_sort(graph))
print(topological_sort(cyclic_graph))