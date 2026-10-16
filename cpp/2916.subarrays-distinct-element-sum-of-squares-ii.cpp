class BinaryIndexTree {
public:
    BinaryIndexTree(int n) : size(n), _tree1(n + 1, 0), _tree2(n + 1, 0) {}

    void add(int left, int right, int delta) {
        _add(left, delta);
        _add(right + 1, -delta);
    }

    long long query(int left, int right) {
        return _query(right) - _query(left - 1);
    }

private:
    int size;
    vector<long long> _tree1;
    vector<long long> _tree2;

    int _lowbit(int index) { return index & -index; }

    void _add(int index, int delta) {
        long long p = index;
        index++;

        while (index <= size) {
            _tree1[index] += delta;
            _tree2[index] += p * delta;
            index += _lowbit(index);
        }
    }

    long long _query(int index) {
        index++;

        if (index > size) {
            index = size;
        }
        long long p = index;

        long long res = 0;
        while (index > 0) {
            res += p * _tree1[index] - _tree2[index];
            index -= _lowbit(index);
        }

        return res;
    }
};

class Solution {
public:
    int sumCounts(vector<int>& nums) {
        const long long MOD = (long long)(1e9) + 7;
        const int n = nums.size();

        long long res = 0, cur = 0;
        BinaryIndexTree bit(n + 1);
        unordered_map<int, int> seen; // index where last this symbol met;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int j = (seen.count(x) ? seen[x] : -1) + 1;

            long long q = bit.query(j, i);

            cur = (cur + 2 * q + i - j + 1) % MOD;
            res = (res + cur) % MOD;

            bit.add(j, i, 1);
            seen[x] = i;
        }

        return res;
    }
};