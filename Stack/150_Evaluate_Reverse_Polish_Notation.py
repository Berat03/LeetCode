"""
looking at other solution,
could easy clean up code but testing for expr initally, and then if not an expression appending to stack
still same time complexity


"""

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
        try:
            tk = int(token)  # will return error if not int
            stack.append(tk)
        except:
            # our first expr, must always follow two numbers (how else??)
            prev_num = stack.pop()
            prev_x2_num = stack.pop()
            if token == '*':
                value = prev_x2_num * prev_num
            elif token == '+':
                value = prev_x2_num + prev_num
            elif token == '-':
                value = prev_x2_num - prev_num
            elif token == '/':
                value = int(float(prev_x2_num) / prev_num)
                """
                Mt machine int(x / y) works
                Leetcode need to add the float (above) else returns -1 for Case 3
                version of python??
                
                """

            stack.append(value)
    assert len(stack) == 1
    return stack[0]  # should only be one value