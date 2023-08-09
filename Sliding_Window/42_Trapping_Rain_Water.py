def bruteforce(height: list[int]) -> int:
    total = 0

    for idx, h in enumerate(height):


        try:
            max_left = max(height[0:idx:])
            max_right = max(height[idx + 1::])  # this already skips it
        except:
            continue # as we have no wall on each side


        vol = min(max_left, max_right) - h
        if vol > 0:
            total += vol
    return total

def trap(height: list[int]) -> int:
    total = 0
    lp, rp = 0, len(height) - 1
    rmax, lmax = height[-1], height[0]
    while lp < rp:
        if lmax < rmax:
            lp += 1
            lmax = max(height[lp], lmax)
            vol = min(rmax, lmax) - height[lp]
            total += max(vol, 0)
        elif lmax > rmax:
            rp -= 1
            rmax = max(height[rp],rmax)
            vol = min(rmax, lmax) - height[rp]
            total += max(vol, 0)
        else:
            lp += 1
            lmax = max(height[lp], lmax)
            vol = min(rmax, lmax) - height[lp]
            total += max(vol, 0)

    return total




print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
