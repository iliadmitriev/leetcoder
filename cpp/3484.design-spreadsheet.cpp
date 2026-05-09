#include <string>
#include <unordered_map>
#include <utility>

using std::string, std::unordered_map, std::pair;

class Spreadsheet {
private:
  unordered_map<string, int> sheet;

public:
  Spreadsheet(int rows) : sheet({}) {}

  void setCell(string cell, int value) { sheet[cell] = value; }

  void resetCell(string cell) { sheet.erase(cell); }

  int getValue(string formula) {
    auto [op1, op2] = parseFormula(formula);

    return celRef(op1) + celRef(op2);
  }

  pair<string, string> parseFormula(string formula) {
    int pos = formula.find('+');
    return {formula.substr(1, pos - 1),
            formula.substr(pos + 1, formula.size() - pos - 1)};
  }

  int celRef(string cell) {
    if (cell[0] >= 'A' && cell[0] <= 'Z') {
      return sheet[cell];
    } else {
      return stoi(cell);
    }
  }
};

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet* obj = new Spreadsheet(rows);
 * obj->setCell(cell,value);
 * obj->resetCell(cell);
 * int param_3 = obj->getValue(formula);
 */