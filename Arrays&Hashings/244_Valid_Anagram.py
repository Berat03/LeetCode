def isAnagram(self, s, t):
    ls = sorted(list(s))
    lt = sorted(list(t))
    return ls == lt
