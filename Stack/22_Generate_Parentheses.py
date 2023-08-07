class Solution:
    def generateParenthesis(n: int) -> list[str]:
        res = []


        def backtrack(open_count, close_count, s):
            if open_count == close_count == n: # full valid solution, 'basecase'
                res.append(s)
                return

            # if statements as to explore both options
            if open_count < n: # if False, then we can only add close
                backtrack(open_count + 1, close_count, s + '(')

            if open_count > close_count:
                backtrack(open_count, close_count + 1, s + ')')


        backtrack(0,0,'')
        return res