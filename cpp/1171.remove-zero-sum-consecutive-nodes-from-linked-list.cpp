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
  ListNode *removeZeroSumSublists(ListNode *head) {
    ListNode *dummy = new ListNode(0, head);
    unordered_map<int, ListNode *> mp;
    mp[0] = dummy;

    ListNode *curr = dummy;
    int total = 0;
    while (curr) {
      total += curr->val;
      mp[total] = curr;
      curr = curr->next;
    }

    vector<ListNode *> dump;

    curr = dummy;
    total = 0;
    while (curr) {
      total += curr->val;
      curr->next = mp[total]->next;
      // nodes to erase
      ListNode *tmp = curr->next;
      while (tmp && tmp != mp[total]) {
        dump.push_back(tmp);
        tmp = tmp->next;
      }

      curr = curr->next;
    }

    return dummy->next;
  }
};