class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        from decimal import Decimal
        
        if not points:
            return 0
        
        slopesObserved = set()
        maxConnections = 0
        duplicateCounter = dict()
        
        for point in points:
            if str(point) in duplicateCounter:
                duplicateCounter[str(point)] += 1
            else:
                duplicateCounter[str(point)] = 0
        
        for i in range(0, len(points)-1):
            firstPoint = points[i]
            currentMaxConnections = 0
            slopesToConnections = defaultdict(int)
            for j in range(i+1, len(points)):
                secondPoint = points[j]
                if secondPoint == firstPoint:
                    continue
                
                deltaY = (points[j][1] - points[i][1])
                deltaX = (points[j][0] - points[i][0])
                if deltaX == 0:
                    slope = float('inf')
                else:
                    slope = Decimal(deltaY) / Decimal(deltaX)
                slopesToConnections[slope] += 1
                currentMaxConnections = max(slopesToConnections[slope]+duplicateCounter[str(firstPoint)], currentMaxConnections)
            maxConnections = max(maxConnections, currentMaxConnections)
            maxConnections = max(maxConnections, duplicateCounter[str(firstPoint)])
        return maxConnections+1
        
