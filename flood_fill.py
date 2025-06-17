"""
Approach: save the initColor for eventual comparisons and start a dfs and explore all neighbors in a dfs 
fashion visiting only the nodes with initColor and paint with given color
t.c.=> O(m * n)
s.c. => O(m * n)
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initColor = image[sr][sc]
        m, n = len(image), len(image[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        if image[sr][sc] == color:
            return image

        def dfs(i, j):
            image[i][j] = color
            for x, y in directions:
                newX, newY = x + i, y + j
                if newX < 0 or newY < 0 or newX >= m or newY >= n or image[newX][newY] != initColor:
                    continue
                dfs(newX, newY)
        dfs(sr, sc)
        return image