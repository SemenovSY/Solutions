def subarraySum(nums, k):
    count = {}
    count[0] = 1
    counter = 0
    s = 0
    for x in nums:
        s += x
        if s - k in count:
            counter += count[s-k]
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
            
    return counter
    
nums = [1,-1,0]
k = 0
print(subarraySum(nums, k))
