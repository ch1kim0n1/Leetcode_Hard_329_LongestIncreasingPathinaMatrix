import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sys.setrecursionlimit(max(100000, m * n + 10))

        dp = [[0] * n for _ in range(m)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            cur = matrix[r][c]
            best = 1

            if r > 0 and matrix[r - 1][c] > cur:
                best = max(best, 1 + dfs(r - 1, c))
            if r + 1 < m and matrix[r + 1][c] > cur:
                best = max(best, 1 + dfs(r + 1, c))
            if c > 0 and matrix[r][c - 1] > cur:
                best = max(best, 1 + dfs(r, c - 1))
            if c + 1 < n and matrix[r][c + 1] > cur:
                best = max(best, 1 + dfs(r, c + 1))

            dp[r][c] = best
            return best

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans
