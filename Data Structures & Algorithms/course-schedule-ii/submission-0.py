class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = set()
        safe = set()
        path = list()

        def dfs(course):
            if course in visited:
                return False
            if course in safe:
                return True
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            safe.add(course)
            path.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return path
        