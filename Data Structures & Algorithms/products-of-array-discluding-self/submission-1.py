class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = [None] * len(nums)
        answer = [None] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                forward.append(nums[i])
                continue;
            forward.append(forward[i-1] * nums[i])
        
        # print("Forward = ", *forward)
        
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1):
                backward[i] = nums[i]
                continue;
            backward[i] = nums[i] * backward[i + 1]
        
        # print("Backward = ", *backward)

        for i in range(0, len(nums)):
            forw = None
            back = None
            if i == 0:
                forw = 1
            else:
                forw = forward[i-1]
            
            if i == (len(nums) - 1):
                backw = 1
            else:
                backw = backward[i + 1]
            
            answer[i] = forw * backw


        return answer
