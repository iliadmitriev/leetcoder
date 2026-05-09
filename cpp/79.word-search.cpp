class Solution {
private:
  bool dfs(const vector<vector<char>> &board, const string &word, int r,
           int c) {

    int m = board.size(), n = board[0].size();
    stack<tuple<int, int, int, bool>> st;
    st.push({r, c, 0, false});

    set<pair<int, int>> visited;
    vector<int> phase = {-1, 0, 1, 0, -1};

    while (!st.empty()) {
      auto [r, c, i, flag] = st.top();
      st.pop();

      if (flag) {
        visited.erase({r, c});
      } else {
        if (i >= word.size()) {
          continue;
        }

        if (word[i] != board[r][c]) {
          continue;
        }

        if (i == word.size() - 1) {
          return true;
        }

        visited.insert({r, c});
        st.push({r, c, i, true});

        for (int j = 0; j < 4; j++) {
          int ny = r + phase[j], nx = c + phase[j + 1];
          if (!(0 <= ny && ny < m && 0 <= nx && nx < n)) {
            continue;
          }

          if (visited.find({ny, nx}) == visited.end()) {
            st.push({ny, nx, i + 1, false});
          }
        }
      }
    }

    return false;
  }

public:
  bool exist(vector<vector<char>> &board, string word) {
    int m = board.size(), n = board[0].size();
    // op 1: word has less letters than board size
    if (word.size() > m * n) {
      return false;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (word[0] == board[i][j] && dfs(board, word, i, j)) {
          return true;
        }
      }
    }

    return false;
  }
};