def reachingPoints(self, sx, sy, tx, ty):
    # Edge Cases
    if sx == tx and sy == ty:
        return True
    if sx > tx or sy > ty:
        return False
    
    def reaching_points_helper(sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return True
        if sx+sy > tx or sx+sy > ty:
            return False
        return reaching_points_helper(sx+sy, sy, tx, ty) or \
                reaching_points_helper(sx, sx+sy, tx, ty)
    
    return reaching_points_helper(sx, sy, tx, ty)
            