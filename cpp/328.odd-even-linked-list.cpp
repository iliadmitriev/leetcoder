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
    ListNode* oddEvenList(ListNode* head) {
        // if there is no head
        if (!head) {
            return head;
        }

        // set odd head on 1st
        // set even head on 2nd
        auto odd_head = head;
        auto even_head = head->next;

        // start current odd and even pointers
        auto odd = odd_head; auto even = even_head;

        // while there is one even and one next odd
        while (even && even->next) {
            // join odd to next odd (skip even)
            odd->next = even->next;
            // move odd pointer forward
            odd = odd->next;

            // join even to next even (skip odd)
            even->next = odd->next;
            // move even pointer forward
            even = even->next;
        }

        // finally, join odd tail to even head
        odd->next = even_head;

        // return odd head
        return odd_head;
    }
};