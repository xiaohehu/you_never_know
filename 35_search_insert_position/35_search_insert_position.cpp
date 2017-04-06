class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            return NULL;
        }
        int ans = 0;
        int start = 0;
        int end = nums.size() - 1;
        while ((start + 1) < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                start = mid;
            }
            if (nums[mid] > target) {
                end = mid;
            }
        }
        if (nums[end] < target) {
            return end + 1;
        }
        if (nums[start] > target) {
            return (start > 0? start - 1 : 0);
        }
        if (nums[end] == target) {
            return end;
        }
        if (nums[start] == target) {
            return start;
        }
        return start + 1;
    }
};
