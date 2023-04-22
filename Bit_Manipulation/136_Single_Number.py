def singleNumber(self, nums):
    numbers = dict()

    for num in nums:

        if not (num in numbers.keys()):
            numbers[num] = 1

        elif num in numbers.keys():
            numbers.pop(num)
    x = numbers.keys()
    return x[0]


def singleNumber(self, nums):
    numbers = dict()

    for num in nums:

        if not (num in numbers.keys()):
            numbers[num] = 1

        elif num in numbers.keys():
            numbers.pop(num)
    x = numbers.keys()
    return x[0]
