class Solution {
public:
    string reorganizeString(string s) {
        vector<int> char_count(26, 0);
        for (char ch : s)
            char_count[ch - 'a']++;

        int max_char = 0;
        int max_char_count = 0; 

        for (int i = 0; i < 26; i++) {
            if (char_count[i] > max_char_count) {
                max_char_count = char_count[i];
                max_char = i;
            };
        };

        // check if goal is achivable;
        if (max_char_count > (s.size() + 1) / 2)
            return string();

        // init res string
        string res(s.size(), '0');
        int index = 0;

        while (char_count[max_char] > 0) {
            res[index] = char('a' + max_char);
            index += 2;
            char_count[max_char]--;
        };
        
        for (int i = 0; i < 26; i++) {
            while (char_count[i] > 0) {
                if (index >= s.size())
                    index = 1;
                
                res[index] = char('a' + i);

                index += 2;
                char_count[i]--;

            };
        };
            
        return res;

    }
};