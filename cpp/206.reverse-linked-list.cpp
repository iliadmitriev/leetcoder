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
  ListNode *reverseList(ListNode *head) {
    ListNode *curr = head, *prev = nullptr, *tmp;
    while (curr) {
      tmp = curr->next;  // save next pointer for next step
      curr->next = prev; // reassing next pointer to previous
      prev = curr;       // move next pointer to current
      curr = tmp;        // move current to saved next step
    }

    return prev;
  }
};