class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def distance(x1,y1,x2,y2):
            return max(abs(x1-x2) , abs(y1-y2))

        result = 0
        for i in range(1, len(points)):
            result += distance(*points[i],*points[i-1])
        return result
