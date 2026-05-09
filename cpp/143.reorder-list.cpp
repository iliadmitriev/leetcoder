/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  void reorderList(ListNode *head) {
    // find the middle
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
      slow = slow->next;
      fast = fast->next->next;
    }

    // split the list into two parts
    ListNode *mid = slow->next;
    slow->next = nullptr;

    // reverse the second part
    ListNode *prev = nullptr, *curr = mid, *tmp;
    while (curr) {
      tmp = curr->next;
      curr->next = prev;
      prev = curr;
      curr = tmp;
    }

    // merge the two parts
    ListNode *p = head, *q = prev;
    ListNode *pp, *qq;
    while (p && q) {
      pp = p;
      qq = q;

      p = p->next;
      q = q->next;

      pp->next = qq;
      qq->next = p;
    }
  }
};