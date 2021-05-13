def combinationSum(candidates, target):
    import copy
    ans = []
    def DFS(i, candidates, target, lst=[]):
        print(lst)
        for j in range(i, len(candidates)):
            if sum(lst) < target:
                lst.append(candidates[j])
                DFS(j, candidates, target, lst)
                if sum(lst) == target:
                    ans.append(copy.deepcopy(lst))
                lst.pop()
    DFS(0, candidates, target)
    return ans
