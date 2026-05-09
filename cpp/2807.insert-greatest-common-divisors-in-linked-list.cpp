
class Solution {
private:
  int _gcd(int a, int b) {
    while (b) {
      int r = a % b;
      a = b;
      b = r;
    }

    return a;
  }

public:
  ListNode *insertGreatestCommonDivisors(ListNode *head) {
    ListNode *cur = head, *mid, *next;

    if (cur == nullptr || cur->next == nullptr) {
      return head;
    }

    next = cur->next;

    while (next) {
      int g = _gcd(cur->val, next->val);
      mid = new ListNode(g);

      cur->next = mid;
      mid->next = next;
      cur = next;
      next = cur->next;
    }

    return head;
  }
};