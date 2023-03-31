def twoSum(nums, target):
    for index, num in enumerate(nums):
        for index2, num2 in enumerate(nums[index + 1:]):
            test = num + num2
            if test == target:
                return [index, index + index2 + 1]


# Tip: Really go slow and be sure of the indexing.

# Much faster solution.
def twoSum2(nums, target):
    d = {}
    for i, num in enumerate(nums):  # Only iterates through list once!
        if target - num in d:
            return [d[target - num], i]
        d[num] = i
    return []
