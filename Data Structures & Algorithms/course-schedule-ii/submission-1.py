class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        path = set()
        safe = set()
        order = list()

        def dfs(course):
            if course in path:
                return False
            if course in safe:
                return True
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            safe.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return order
        