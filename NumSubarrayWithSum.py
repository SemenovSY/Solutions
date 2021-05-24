def numSubarrayWithSum(nums, goal):
    count = {}
    count[0] = 1
    counter = 0
    s = 0
    for x in nums:
        s += x
        if s - goal in count:
            counter += count[s-goal]
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
            
    return counter
    
nums = [1,0,1,0,1]
goal = 2
print(numSubarrayWithSum(nums, goal))
