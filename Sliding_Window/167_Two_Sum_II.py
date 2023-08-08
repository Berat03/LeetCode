class Solution:
    def twoSum(numbers: list[int], target: int) -> list[int]:
        right = len(numbers) - 1

        for left in range(len(numbers)):
            while numbers[left] + numbers[right] > target:
                numbers.pop()
                right -= 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

