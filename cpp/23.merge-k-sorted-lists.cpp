/**
 * Definition for singly-linked list.
 */
#include <deque>
#include <vector>

// struct ListNode {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

using namespace std;

class Solution {
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
        list1 = list1->next;
      } else {
        cur->next = list2;
        list2 = list2->next;
      }
      cur = cur->next;
    }

    cur->next = list1 ? list1 : list2;
    cur = result->next;
    delete result;

    return cur;
  }

public:
  ListNode *mergeKLists(vector<ListNode *> &lists) {
    deque<ListNode *> q(lists.begin(), lists.end());

    ListNode *list1, *list2;
    while (q.size() > 1) {
      list1 = q.front();
      q.pop_front();
      list2 = q.front();
      q.pop_front();

      q.push_back(mergeTwoLists(list1, list2));
    }

    return q.size() ? q.front() : nullptr;
  }
};