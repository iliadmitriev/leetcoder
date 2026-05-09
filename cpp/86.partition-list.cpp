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
    ListNode* partition(ListNode* head, int x) {
        ListNode* less_head = new ListNode(); ListNode* other_head = new ListNode();
        ListNode* less_tail = less_head; ListNode* other_tail = other_head;

        while (head) {
            if (head->val < x) {
                less_tail->next = head;
                less_tail = less_tail->next;
            } else {
                other_tail->next = head;
                other_tail = other_tail->next;
            }
            head = head->next;
        }

        less_tail->next = other_head->next;
        other_tail->next = NULL;
        head = less_head->next;

        delete less_head; delete other_head;
        
        return head;
        
    }
};