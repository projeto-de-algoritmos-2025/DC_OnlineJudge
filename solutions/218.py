class Solution:
    def getSkyline(self, buildings):
        if not buildings:
            return []
        if len(buildings) == 1:
            L, R, H = buildings[0]
            return [[L, H], [R, 0]]

        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        h1 = h2 = 0
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else:
                x = left[i][0]
                h1 = left[i][1]
                h2 = right[j][1]
                i += 1
                j += 1
            maxH = max(h1, h2)
            if not result or result[-1][1] != maxH:
                result.append([x, maxH])
        result.extend(left[i:])
        result.extend(right[j:])
        return result
