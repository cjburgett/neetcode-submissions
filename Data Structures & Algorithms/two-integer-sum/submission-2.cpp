class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;

        for (int i = 0; i < nums.size(); i++) {
            // case 1 where target is found yay
            if (um.contains(target - nums[i])) {
                int temp = um[target - nums[i]];
                vector<int> answer = {temp, i};
                return answer;
            } else {
                // mp["Apple"] = 10;
                um[nums[i]] = i;
            }
        }
        return {};
    }
};
