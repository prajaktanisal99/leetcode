class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i: [] for i in range(numCourses)}

        # adjacency list
        for course, pre in prerequisites:
            preReqMap[course].append(pre)

        # cycle detection
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preReqMap[course] == []:
                return True

            visited.add(course)
            for p in preReqMap[course]:
                if not dfs(p):
                    return False

            visited.remove(course)
            preReqMap[course] = []
            return True

        # check for all the nodes. Handles test cases that does not contain fully connected graph.
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
