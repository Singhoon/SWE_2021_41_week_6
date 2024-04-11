from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numdictionary = {}
    for i, num in enumerate(nums):
        k = target - num
        if complement in numdictionary:
            return [numdictionary[k], i]
        numdictopmaru[num] = i