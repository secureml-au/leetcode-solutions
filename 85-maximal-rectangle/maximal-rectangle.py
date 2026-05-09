class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        def largestRect(heights):
            stack = []
            max_area = 0
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    H = heights[stack.pop()]
                    W = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, H * W)
                stack.append(i)
            heights.pop()
            return max_area

        cols = len(matrix[0])
        heights = [0] * cols
        res = 0

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            res = max(res, largestRect(heights))
        return res