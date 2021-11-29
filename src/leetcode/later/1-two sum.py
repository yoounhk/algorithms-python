from typing import List

# TODO: 브루트 포스가 아닌 방법으로 풀어보기


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
