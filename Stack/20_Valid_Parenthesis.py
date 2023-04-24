def isValid(self, s):
    stack = []
    map = {')': '(', '}': '{', ']': '['}

    for p in s:
        if p not in map:  # if its not a key, so its a legal opening bracket
            stack.append(p)
            continue
        if not stack or stack[-1] != map[p]:
            return False
        stack.pop()
    return not stack