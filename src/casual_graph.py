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


def has_path(graph,start,target):
    if start==target:
        return True
    for child in graph[start]:
        if has_path(graph,child,target):
            return True
    return False
print(has_path(graph, "motivation", "exam_score"))
print(has_path(graph, "motivation", "study_hours"))
print(has_path(graph, "study_hours", "motivation"))
print(has_path(graph, "exam_score", "motivation"))

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

print(has_cycle(graph))        
print(has_cycle(cyclic_graph))  