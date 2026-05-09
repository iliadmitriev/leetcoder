
class RangeTreeNode {
private:
  int start, end;
  RangeTreeNode *left, *right;

public:
  RangeTreeNode(int start, int end)
      : start(start), end(end), left(nullptr), right(nullptr){};

  bool insert(int _start, int _end) {
    if (_end <= this->start) {

      if (!this->left) {
        this->left = new RangeTreeNode(_start, _end);
        return true;
      }

      return this->left->insert(_start, _end);

    } else if (this->end <= _start) {

      if (!this->right) {
        this->right = new RangeTreeNode(_start, _end);
        return true;
      }

      return this->right->insert(_start, _end);
    }

    return false;
  }
};

class MyCalendar {
public:
  RangeTreeNode *root;
  MyCalendar() : root(nullptr) {}

  bool book(int start, int end) {

    if (!root) {
      root = new RangeTreeNode(start, end);
      return true;
    }

    return root->insert(start, end);
  }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */