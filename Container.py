def container(height):

    left = 0
    right = len(height)-1

    max_area = 0
    #area = min(left, right) *
    while left < right:
        
        left_height = height[left]
        right_height = height[right]

        area = min(left_height, right_height) * (right-left)

        if area > max_area:
            max_area = area

        if left_height >= right_height:
            right -= 1
            
        else:
            left += 1

    return max_area
