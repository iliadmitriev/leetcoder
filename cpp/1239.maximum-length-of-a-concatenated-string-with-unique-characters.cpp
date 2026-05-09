class Solution {
private:
    unordered_map<int, int> cache;

    int mask(string& s) {
        int res = 0;
        for (auto ch: s) {
            res |= 1 << (ch - 'a');
        }

        return res;
    }

    int uniqLen(string& s) {
        vector<bool> cache(26, false);
        int res = 0;
        for (auto ch: s) {
            if (cache[ch - 'a']) {
                continue;
            }
            res++;
            cache[ch - 'a'] = true;
        }

        return res;
    }

    int dp(vector<int>& masked, vector<int>& lens, int curMask, int curLen, int idx) {
        if (idx == masked.size()) {
            return curLen;
        }

        if (cache.find(curMask) != cache.end()) {
            return cache[curMask];
        }

        int res = curLen;
        for (int i = idx; i < masked.size(); i++) {
            if (!(curMask & masked[i])) {
                int newLen = dp(masked, lens, curMask | masked[i], curLen + lens[i], i + 1);
                res = max(res, newLen);
            }
        }

        return cache[curMask] = res;
    }

public:
    Solution(): cache({}) {}

    int maxLength(vector<string>& arr) {
        vector<string> filtered;
        for (int i = 0; i < arr.size(); i++) {
            if (uniqLen(arr[i]) == arr[i].size()) {
                filtered.push_back(arr[i]);
            }
        }

        vector<int> masked(filtered.size(), 0);
        vector<int> lens(filtered.size(), 0);
        for (int i = 0; i < filtered.size(); i++) {
            masked[i] = mask(filtered[i]);
            lens[i] = filtered[i].size();
        }

        return dp(masked, lens, 0, 0, 0);
    }
};