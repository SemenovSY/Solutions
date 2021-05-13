def sortColors(nums):
    z = 0
    o = 0
    t = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            z += 1
        elif nums[i] == 1:
            o += 1
        else:
            t += 1

    nums = [0]*z + [1]*o + [2]*t
    return(nums)

print(sortColors([2,0,2,1,1,0]))
