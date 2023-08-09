def maxArea(height: list[int]) -> int:
    r = (len(height) - 1)
    l = 0
    res = 0
    while l < r:
        vol = min(height[l], height[r])  * (r - l)
        res = max(res, vol)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res