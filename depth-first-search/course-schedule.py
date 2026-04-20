class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = []
        order = []
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        while q:
            u = q.pop(0)
            order.append(u)
            for nei in graph[u]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(order) != numCourses:
            return False
        return True