def inRotated(nums, target):

    if target == nums[0]:
        return 0
    
    else:
        new_arr = []
        for elem in nums[::-1]:
            if elem < nums[0]:
                new_arr.append(nums.pop())
        first = nums[0]
        if new_arr:
            plus = len(nums)
        else:
            plus = 0
        nums = new_arr[::-1] + nums

        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while nums[mid] != target and start < end:
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

            mid = (start + end) // 2
            
        if nums[mid] != target:
            return -1
        
        if target > first:
            return mid - plus
        
        else:
            return mid + plus
