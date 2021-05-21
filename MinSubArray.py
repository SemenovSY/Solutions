def minSubArray(nums, s):
    if sum(nums) < s:
        return ''

    total = left = 0
    result = len(nums) + 1
    min_ = nums.copy()

    for right, n in enumerate(nums):
        total += n
        while total >= s:
            if len(nums[left:right+1]) < len(min_):
                min_ = nums[left:right+1]
            total -= nums[left]
            left += 1

    return ' '.join(map(str, min_))

array = list(map(int, input().split()))
N = int(input())
print (minSubArray(array, N))
