def binary(nums, target):
    if nums:
        start = 0
        end = len(nums) - 1

        mid = (end + start) // 2

        while nums[mid] != target and start < end:
            if nums[mid] > target:
                end = mid - 1
                
            elif nums[mid] < target:
                start = mid + 1

            mid = (end + start) // 2
        if start > end:
            return [-1, -1]
        else:
            return mid


    
    


    
            
        
