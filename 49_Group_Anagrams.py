def groupAnagrams(strs):
    d = {}
    for word in strs:
        key = str(sorted(word))
        if key not in d:
            d[key] = []
        d[key].append(word)
    return list(d.values())

#  'for key in d' in almost x10 faster than 'for key in d.keys()'