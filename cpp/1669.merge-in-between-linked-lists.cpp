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
  ListNode *mergeInBetween(ListNode *list1, int a, int b, ListNode *list2) {
    ListNode *p1 = list1, *p2 = list1;

    for (; a > 1; a--)
      p1 = p1->next;

    for (; b > 0; b--)
      p2 = p2->next;

    p1->next = list2;

    for (p1 = list2; p1->next; p1 = p1->next)
      ;

    p1->next = p2->next;
    p2->next = NULL;

    return list1;
  }
};