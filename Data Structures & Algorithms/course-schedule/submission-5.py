class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)

        path = set()

        def cycle(course):
            if course in path:
                return True
            if course not in graph or not graph[course]:
                return False
            path.add(course)
            for prereq in graph[course]:
                if cycle(prereq):
                    return True
            path.remove(course)
            graph[course] = []
            return False

        for course in graph:
            if cycle(course):
                return False
        return True
