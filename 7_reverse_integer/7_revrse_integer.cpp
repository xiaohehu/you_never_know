class Solution {
public:
    int reverse(int x) {
        long result = 0;
        int tempx = x;
        x = abs(x);
        if (x == 0) {
            return result;
        }
        vector<int> numberList;
        while (x > 0) {
            numberList.push_back(x % 10);
            x = x / 10;
        }
        for (int i = 0; i < numberList.size(); i++) {
            result = result + numberList[numberList.size() - 1 - i] * pow(10 , i);
        }
        if (result > (pow(2, 31) - 1)) {
            return 0;
        }
        if (tempx < 0) {
            return -result;
        }
        return result;
    }
};
