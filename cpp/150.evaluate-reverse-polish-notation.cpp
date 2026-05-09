class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        map<string, function<int(int,int)>> op = {
            { "+", [](int a, int b) -> int { return a + b; } },
            { "-", [](int a, int b) -> int { return a - b; } },
            { "*", [](int a, int b) -> int { return a * b; } },
            { "/", [](int a, int b) -> int { return a / b; } }
        };

        stack<int> st;

        for (const string& token: tokens) {
            if (op.find(token) != op.end()) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                st.push(op[token](a, b));
            } else {
                st.push(stoi(token));
            }
        }

        return st.top();
    }
};