def productExceptSelf(nums):
    result = []
    for i in range(len(nums)):
        i_nums = nums[i]
        nums[i] = 1
        product = 1
        for j in range(len(nums)):
            product *= nums[j]
        nums[i] = i_nums
        result.append(product)

        return result


# Not efficient enough, need O(n) time complexity but this is O(n^2)

def productExceptSelf(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
    return result

# Smart solution
# Think, do I need to go in the same direction again? Or can I do two individual runs?
