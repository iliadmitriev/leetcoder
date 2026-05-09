#include <vector>
using std::vector;

const int MOD = 1e9 + 7;

class Matrix {
private:
  int rows, cols;
  vector<vector<long>> mat;

public:
  Matrix(const vector<vector<long>> &m)
      : rows(m.size()), cols(m[0].size()), mat(m) {}

  Matrix(int r, int c) : rows(r), cols(c), mat(r, vector<long>(c, 0)) {}

  const vector<long> &operator[](int i) const { return mat[i]; }

  Matrix operator*(const Matrix &other) {
    Matrix result(rows, other.cols);
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < other.cols; j++) {
        for (int k = 0; k < cols; k++) {
          result.mat[i][j] =
              (result.mat[i][j] + mat[i][k] * other.mat[k][j]) % MOD;
        }
      }
    }
    return result;
  }

  // matrix modular exponentiation
  // returns the matrix raised to the power of exp with modulo
  Matrix pow(int exp) {
    Matrix result(rows, cols);
    for (int i = 0; i < rows; i++) {
      result.mat[i][i] = 1;
    }
    Matrix base = *this;
    while (exp) {
      if (exp & 1) {
        result = result * base;
      }
      base = base * base;
      exp >>= 1;
    }
    return result;
  }
};

class Solution {
private:
  void genStates(int m, vector<int> &curState, vector<vector<int>> &res) {
    if (m == curState.size()) {
      res.push_back(curState);
      return;
    }

    for (int color = 1; color <= 3; color++) {
      if (curState.size() && curState.back() == color) {
        continue;
      }

      curState.push_back(color);
      genStates(m, curState, res);
      curState.pop_back();
    }
  }

  bool canBeAdjacent(const vector<int> &a, const vector<int> &b) {
    const int n = a.size();
    for (int i = 0; i < n; i++) {
      if (a[i] == b[i]) {
        return false;
      }
    }
    return true;
  }

  vector<vector<long>> buildAdjacencyMatrix(vector<vector<int>> &states) {
    const int k = states.size();
    vector<vector<long>> res(k, vector<long>(k, 0));

    for (int i = 0; i < k; i++) {
      for (int j = 0; j < k; j++) {
        if (canBeAdjacent(states[i], states[j])) {
          res[i][j] = 1;
        }
      }
    }
    return res;
  }

public:
  int colorTheGrid(int m, int n) {
    long total = 0;
    vector<vector<int>> states;
    vector<int> state;
    genStates(m, state, states);

    if (n == 1) {
      return states.size();
    }

    vector<vector<long>> adj = buildAdjacencyMatrix(states);

    Matrix mat(adj);

    Matrix res = mat.pow(n - 1);

    for (int i = 0; i < states.size(); i++) {
      for (int j = 0; j < states.size(); j++) {
        total = (total + res[i][j]) % MOD;
      }
    }

    return total;
  }
};