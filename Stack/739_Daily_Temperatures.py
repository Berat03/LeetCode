def montonic(temperatures):
    ans = []
    while len(temperatures) != 0:
        if len(temperatures) == 1:
            ans.append(0)
            return ans
        leng = len(temperatures)
        c = 0
        current_day = temperatures[0]
        for i in range(1, leng):
            next_day = temperatures[i]
            if current_day < next_day:
                c += 1
                break
            elif current_day >= next_day and i == (leng-1):
                break
            c += 1
        ans.append(c)
        temperatures = temperatures[1::]

def dailyTemperatures(temperatures):
    stack = [] #[idx, temp]
    res = [0] * len(temperatures)

    for idx, temp in enumerate(temperatures):
        while len(stack) != 0 and temp > stack[-1][1]:
            stk_idx, stk_tmep = stack.pop()
            res[stk_idx] = (idx - stk_idx)

        stack.append((idx, temp))
    return res

def check():
    assert(dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    assert(dailyTemperatures([30,40,50,60]) == [1,1,1,0])
    assert(dailyTemperatures([30,60,90]) == [1,1,0])
    assert(dailyTemperatures([68]) == [0])


check()







