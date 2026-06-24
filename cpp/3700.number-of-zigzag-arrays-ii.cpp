static constexpr int MOD = int(1e9) + 7;
// flatten matrix to vector: x[i * m + j] = X[i][j]
using matrix = vector<int>;

static int m;
// operator * for matrix
static inline matrix operator*(const matrix& A, const matrix& B) {
    matrix C(m * m, 0);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (A[i * m + j] == 0) {
                continue; // matrix is sparce, a lot of 0's
                          // skip those lines
            }

            for (int k = 0; k < m; k++) {
                C[i * m + k] =
                    (C[i * m + k] + 1LL * A[i * m + j] * B[j * m + k]) % MOD;
            }
        }
    }

    return C;
}

static matrix I() {
    matrix ans(m * m, 0);
    for (int i = 0; i < m; i++) {
        ans[i * m + i] = 1;
    }
    return ans;
}

// MSBF modular matrix exponentiation
static matrix pow(matrix M, unsigned exp) {
    matrix res = I();

    for (; exp; exp >>= 1) {
        if (exp & 1) {
            res = res * M;
        }

        M = M * M;
    }

    return res;
}

class Solution {

public:
    int zigZagArrays(int n, int l, int r) {
        m = r - l + 1; // assing matrix size to a global state
        
        matrix U(m * m, 0), L(m * m, 0);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < i; j++) {
                L[i * m + j] = 1;
            }

            for (int j = i + 1; j < m; j++) {
                U[i * m + j] = 1;
            }
        }

        n--;

        const int n0 = n >> 1;
        const matrix UL = U * L;
        matrix P = pow(UL, n0);

        if (n & 1) {
            P = L * P;
        }

        return 2LL * reduce(P.begin(), P.end(), 0LL) % MOD;
    }
};