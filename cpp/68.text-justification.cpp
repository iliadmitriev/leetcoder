class Solution {
private:
    // Count words than fit into the line of max_width starting from the i-th word
    vector<string> get_words(int i, int max_width, vector<string>& words) {
        vector<string> curr_line;
        int curr_length = 0;

        while (i < words.size() && curr_length + words[i].size() <= max_width) {
            curr_line.push_back(words[i]);
            curr_length += words[i].size() + 1; // +1 for space
            i += 1;
        }

        return curr_line;
    }

    string build_line(vector<string>& line, int i, int max_width, vector<string> words) {
        int base_length = -1;
        for (const auto& word : line)
            base_length += word.size() + 1;
        
        int extra_spaces = max_width - base_length;

        // if it's a last line or a line consists of one word
        // join the line and add extra spaces ath the end
        if (i == words.size() || line.size() == 1)
            return join(line) + string(extra_spaces, ' ');


        int word_count = line.size() - 1;
        int spaces_per_word = extra_spaces / word_count;
        int needs_extra_space = extra_spaces % word_count;

        for (int j = 0; j < needs_extra_space; j++)
            line[j] += " ";
        
        for (int j = 0; j < word_count; j++)
            line[j] += string(spaces_per_word, ' ');

        return join(line);

    }

    string join(const vector<string>& v, const string & delimiter = " ") {
        string res;
        if (auto i = v.begin(), e = v.end(); i != e) {
            res += *i++;
            for (; i != e; ++i) res.append(delimiter).append(*i);
        }
        return res;
    }

public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i = 0;

        while (i < words.size()) {
            vector<string> curr_line = get_words(i, maxWidth, words);
            i += curr_line.size();
            res.push_back(build_line(curr_line, i, maxWidth, words));
        };

        return res;
    }
};