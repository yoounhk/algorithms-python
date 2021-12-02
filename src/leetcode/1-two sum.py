from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    #  보수를 활용한 풀이 in을 사용해 O(n^2)이지만 브루트 포스보다 좀 더 빠르다
    """ 
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums[i+1:]:
            return [i, nums[i+1:].index(complement) + i + 1]
    """

    # 딕셔너리를 활용해 비교나 탐색을 하지 않고 구한 풀이
    """
    nums_map = {}
    for i in range(len(nums)):
        nums_map[nums[i]] = i

    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target - n]:
            return [i, nums_map[target - n]]
    """

    # 딕셔너리를 활용하며 반복문을 하나로 줄인 풀이
    """
    nums_map = {}
    for i, n in enumerate(nums):
        if target - n in nums_map:
            return [nums_map[target - n], i]
        nums_map[n] = i
    """
