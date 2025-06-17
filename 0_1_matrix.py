"""
Approach: Do a BFS from 0 to 1. every time they visit the node 1 with the smallest distance
t.c. => O(m* n)
s.c. => O(min(m, n))
"""
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append([i, j, 1])
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        
        visited = set()
        while q:
            x, y, dist = q.popleft()
            
            for i, j in directions:
                newX, newY = x + i, y + j
                if newX < 0 or newY < 0 or newX >=len(mat) or newY >= len(mat[0]) or mat[newX][newY] == 0 or (newX, newY) in visited:
                    continue
                visited.add((newX, newY))
                mat[newX][newY] = dist
                q.append([newX, newY, dist + 1])
        return mat