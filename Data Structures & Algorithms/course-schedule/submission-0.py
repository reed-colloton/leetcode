class Node:
    def __init__(self, course: int):
        self.children = set()


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = Node(course)
            graph[course].children.add(prereq)

        visited = set()

        def cycle(course):
            if course in visited:
                return True
            if course not in graph or not graph[course].children:
                return False
            visited.add(course)
            for prereq in graph[course].children:
                if cycle(prereq):
                    return True
            visited.remove(course)
            return False

        for course in graph:
            if cycle(course):
                return False
        return True