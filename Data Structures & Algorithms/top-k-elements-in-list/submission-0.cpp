class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> um;

        for (int i: nums){
            um[i]++;
        }

        vector<pair<int, int>> sorted;

        for(const auto& num: um) {
            sorted.push_back({num.second, num.first});
        }
        sort(sorted.rbegin(), sorted.rend());

        vector<int> ans;

        for(int i = 0; i < k; i++) {
            ans.push_back(sorted[i].second);
        }

        return ans;


    }
};
