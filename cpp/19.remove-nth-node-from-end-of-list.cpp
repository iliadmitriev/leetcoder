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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* end = head;

        while (n && end) {
            end = end->next;
            n--;
        }

        if (n) {
            return head;
        }

        ListNode* prev = new ListNode();
        ListNode* start = head;
        ListNode* tmp = prev;
        prev->next = start; 

        while (end) {
            prev = start;
            start = start->next;
            end = end->next;
        }

        prev->next = start->next;
        ListNode* res = tmp->next;
        delete tmp;

        if (start) {
            delete start;
        }

        return res;
    }
};