class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for origin, dest in sorted(tickets, reverse=True):
            graph[origin].append(dest)
        
        path = []
        stack = ['JFK']

        while stack:
            origin = stack[-1]
            if not graph[origin]:
                path.append(stack.pop())
            else:
                stack.append(graph[origin].pop())
                
        return list(reversed(path))
