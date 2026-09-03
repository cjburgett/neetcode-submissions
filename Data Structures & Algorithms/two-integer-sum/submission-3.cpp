class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;

        for (int i = 0; i < nums.size(); i++) {
            if (um.contains(target - nums[i])) {
                int temp = um[target - nums[i]];
                vector<int> answer = {temp, i};
                return answer;
            } else {
                um[nums[i]] = i;
            }
        }
        return {};
    }
};
