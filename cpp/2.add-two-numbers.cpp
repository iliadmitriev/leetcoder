class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int d1, d2, res = 0, carry = 0;

    ListNode *dummy = new ListNode();
    ListNode *cur = dummy;

    while (l1 || l2) {
      d1 = d2 = 0;

      if (l1) {
        d1 = l1->val;
        l1 = l1->next;
      }

      if (l2) {
        d2 = l2->val;
        l2 = l2->next;
      }

      res = d1 + d2 + carry;
      carry = res / 10;
      cur->next = new ListNode(res % 10);
      cur = cur->next;
    }

    if (carry) {
      cur->next = new ListNode(carry);
    }

    ListNode *out = dummy->next;
    delete dummy;
    return out;
  }
};