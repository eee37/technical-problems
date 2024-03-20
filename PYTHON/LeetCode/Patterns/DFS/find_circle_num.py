from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0] * len(isConnected)
        count = 0

        for root_index in range(len(isConnected)):
            if visited[root_index] == 0:
                count += 1
                visited[root_index] = 1
                self.dfs(root_index, isConnected, visited)

        return count

    def dfs(self, root_index: int, isConnected: List[List[int]], visited: List[int]):
        print(visited)
        current_row = isConnected[root_index]
        for visiting_index, visited in enumerate(current_row):
            print(visiting_index)
            if visited[visiting_index] == 0 and visited == 1:
                visited[visiting_index] = 1
                self.dfs(visiting_index, isConnected, visited)


