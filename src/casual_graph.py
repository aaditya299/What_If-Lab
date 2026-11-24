graph = {
    "motivation": ["study_hours", "exam_score"],
    "study_hours": ["exam_score"],
    "exam_score": []
}
print(graph)

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