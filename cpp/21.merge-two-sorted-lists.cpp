/**
 * Definition for singly-linked list.
 */
// struct ListNode {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    if (!list1)
      return list2;
    if (!list2)
      return list1;

    ListNode *result = new ListNode();
    ListNode *cur = result;

    while (list1 && list2) {
      if (list1->val < list2->val) {
        cur->next = list1;
        cur = cur->next;
        list1 = list1->next;
      } else {
        cur->next = list2;
        cur = cur->next;
        list2 = list2->next;
      }
    }

    if (list1) {
      cur->next = list1;
    } else {
      cur->next = list2;
    }

    cur = result->next;
    delete result;

    return cur;
  }
};