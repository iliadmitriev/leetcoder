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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *prev = nullptr, *mid = head, *end = head;

        while (end && end->next) {
            prev = mid;
            mid = mid->next;
            end = end->next->next;
        }

        if (!prev) {
            return nullptr;
        }

        if (mid) {
            prev->next = mid->next;
        }

        return head;
    }
};