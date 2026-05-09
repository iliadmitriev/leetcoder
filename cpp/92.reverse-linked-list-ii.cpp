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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // init false start
        ListNode* start = new ListNode(-1, head);

        // init previous and current pointers
        auto pre = start, cur = start->next;

        // find left pointer and previous of left pointer
        for (int i = 1; i < left; i++) {
            pre = pre->next;
            cur = cur->next;
        }

        // reverse
        for (int i = 0; i < right - left; i++) {
            auto tmp = cur->next; // set temp pointer next after current
            cur->next = tmp->next; // link current to next after temp
            tmp->next = pre->next; // link temp to next after previous
            pre->next = tmp; // link previous to temp
        }

        // return next after false start
        head = start->next;
        delete start; // release memory
        return head;
    }
};