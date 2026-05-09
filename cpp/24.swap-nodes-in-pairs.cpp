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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }

        ListNode* dummy = new ListNode(-1, head);

        ListNode* prev = dummy;
        ListNode* cur = head;
        ListNode* second;
        ListNode* step;

        // loop while there is two non-empty pointers
        // available next to each other
        while (cur && cur->next) {
            second = cur->next;
            step = second->next;

            swap(prev->next, cur->next);
            swap(cur->next, second->next);

            prev = cur;
            cur = step;
        }

        ListNode* res = dummy->next;
        delete dummy;
        return res;
    }
};