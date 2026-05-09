class Solution {
private:
    int countDevices(string& row) {
        int count = 0;
        for (auto ch: row) {
            count += ch - '0';
        }

        return count;
    }

public:
    int numberOfBeams(vector<string>& bank) {
        int beams = 0;
        int prev = 0, cur = 0;
        int counter = 0;

        for (auto& row : bank) {
            counter = countDevices(row);
            if (counter > 0) {
                prev = cur;
                cur = counter;
                beams += (cur * prev);
            }
        }

        return beams;
    }
};