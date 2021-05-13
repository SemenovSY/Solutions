def kClosest(points, k):
    count = len(points)
    p_ans = []
    
    if count == 1:
        return points[0]
    
    for i in range(count):
        rng = abs(points[i][0])**2 + abs(points[i][1])**2
        p_ans.append([rng, points[i]])

    p_ans.sort()

    return list(p_ans[i][1] for i in range(k))


points = [[1,3],[-2,2],[2,-2]]
k = 2
print(kClosest(points, k))
