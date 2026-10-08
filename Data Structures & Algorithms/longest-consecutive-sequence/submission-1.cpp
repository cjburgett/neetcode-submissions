class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> contains1;
        set<int> visited;
        

        for (int num: nums){
            contains1.insert(num);
        }
        
        int max_val = 0;
        int counter = 0;
        for (int num: contains1) {
            if (!visited.contains(num)) {
                int value = num;
                counter = 0;
                while (contains1.contains(value)) {
                    counter++;
                    visited.insert(value);
                    value++;
                    
                }
            }
            max_val = max(max_val, counter);
        }
        return max_val;

    }
};
