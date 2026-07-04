class Node:
    def __init__(self):
        self.children = set()


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = Node()
            graph[course].children.add(prereq)

        path = set()
        safe = set()

        def cycle(course):
            if course in path:
                return True
            if (
                course not in graph or 
                not graph[course].children or
                course in safe
            ):
                return False
            path.add(course)
            for prereq in graph[course].children:
                if cycle(prereq):
                    return True
            path.remove(course)
            safe.add(course)
            return False

        for course in graph:
            if cycle(course):
                return False
        return True