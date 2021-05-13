def canJump(nums):
    reach = 0
    idx = 0

    while reach < len(nums) - 1:
        reach = max(reach, idx + nums[idx])

        if idx + 1 <= reach:
            idx += 1

        else:
            return False

    return True
