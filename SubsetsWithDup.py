def subsetsWithDup(nums):
    ans = []
    nums.sort()
    dfs(nums, 0, [], ans)
    return ans

def dfs(nums, idx, path, ans):
    ans.append(path)
    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        dfs(nums, i+1, path+[nums[i]], ans)

print(subsetsWithDup([1,2,2]))
