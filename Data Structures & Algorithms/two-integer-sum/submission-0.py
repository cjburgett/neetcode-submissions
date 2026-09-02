class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i, num in enumerate(nums):
            if (target - num) not in targets:
                targets[num] = i
            else:
                answer = [targets[target - num], i]
                return answer
        
        return []

        