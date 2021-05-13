def search(nums, target):
    
    if nums:
        i = 0
        start = -1
        
        while i < len(nums):
            if nums[i] != target:
                i += 1
            else:
                start = i
                break
        if start >= 0:
            for i in range(len(nums)-1,start-1, -1):
                if nums[i] == target:
                    end = i
                    break
                
            return [start, end]
        else:
            return [-1, -1]
    else:
        return [-1, -1]
