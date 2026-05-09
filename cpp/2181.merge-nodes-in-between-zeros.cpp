
class Solution {
public:
  ListNode *mergeNodes(ListNode *head) {
    ListNode *tmp = new ListNode();
    ListNode *cur = tmp;

    while (head && head->next) {
      if (head->val == 0) {
        cur->next = new ListNode();
        cur = cur->next;
      } else {
        cur->val += head->val;
      }

      head = head->next;
    }

    ListNode *res = tmp->next;
    delete tmp;

    return res;
  }
};