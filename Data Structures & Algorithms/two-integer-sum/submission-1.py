class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Easy problem but 2 things to note:
            # 1. need to be careful in reading full problem
            # 2. even on easy practice writing down logic like in interview
        targets = {}

        for i, num in enumerate(nums):
            if (target - num) in targets:
                answer = [targets[target - num], i]
                return answer
            else:
                targets[num] = i
        
        return []

        