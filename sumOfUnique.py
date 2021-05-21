def sumOfUnique(nums):
    uniq = {}
    for num in nums:
        if num not in uniq:
            uniq[num] = 1
        else:
            uniq[num] += 1
    keys = list(uniq.keys())
    for key in keys:
        if uniq[key] > 1:
            del uniq[key]
    return sum(uniq.keys())

'''def sumOfUnique(nums):
    res = 0
    
    for num in nums:
        if nums.count(num) == 1:
            res += num

    return res'''

nums = [1,2,3,2]
print(sumOfUnique(nums))
