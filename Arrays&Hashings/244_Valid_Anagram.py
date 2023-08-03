def isAnagram(s, t):
    return sorted(s) == sorted(t)

# Sorting in Python is O(nlogn)

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dic_s, dic_t = {}, {}
    for i in range(len(s)):
        dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
        dic_t[t[i]] = 1 + dic_t.get(t[i], 0)
    return dic_s == dic_t
