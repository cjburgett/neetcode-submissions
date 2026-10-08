class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set()

        for num in nums:
            contains.add(num)
        
        visited = set()
        max_counter = 0
        for num in contains:
            if num not in visited:
                value = num
                count = 0
                while value in contains:
                    visited.add(value)
                    count += 1
                    value += 1
                max_counter = max(count, max_counter)
        
        return max_counter


        