#include <stack>
#include <string>

using std::string, std::stack;

class Solution {
private:
  char evaluate(const string &exp, char op) {

    if (op == '!') {
      return exp[0] == 't' ? 'f' : 't';
    } else if (op == '&') {
      for (char tok : exp) {
        if (tok == 'f') {
          return 'f';
        }
      }

      return 't';
    } else if (op == '|') {
      for (char tok : exp) {
        if (tok == 't') {
          return 't';
        }
      }
      return 'f';
    }

    return exp.back();
  }

public:
  bool parseBoolExpr(string expression) {
    stack<char> st;

    for (char tok : expression) {

      if (tok == ',') {
        continue;
      }

      if (tok == '!' || tok == '&' || tok == '|') {
        st.push(tok);
      } else if (tok == '(') {
        continue;
      } else if (tok == ')') {
        string exp;

        while (st.size() && (st.top() == 't' || st.top() == 'f')) {
          exp.push_back(st.top());
          st.pop();
        }

        char op = st.top();
        st.pop();
        st.push(evaluate(exp, op));

      } else if (tok == 't' || tok == 'f') {
        st.push(tok);
      }
    }

    return st.top() == 't' ? true : false;
  }
};