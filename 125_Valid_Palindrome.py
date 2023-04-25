def isPalindrome(s):
    s = s.lower()
    for i in s:
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            s = s.replace(i, '')

    if len(s) == 1 or len(s) == 0:
        return True

    if not s:
        return False

    if s[0] != s[-1]:  # if current palindrome
        return False
    else:
        return isPalindrome(s[1:-1])


print(isPalindrome("hellelleh"))