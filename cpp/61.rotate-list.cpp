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
    ListNode* rotateRight(ListNode* head, int k) {
        // if list consist of 0 or 1 node, then nothing to do
        if (!head or !head->next) {
            return head;
        }

        // count full length of linked list
        // and find one but last node
        auto last = head;
        int count = 0;
        for (auto ptr = head; ptr; ptr = ptr->next) {
            last = ptr;
            count++;
        }

        // reduce k
        k %= count;

        // if it'as a full rotate, then nothing to rotate,
        //  return head as it is
        if (k == 0) {
            return head;
        }

        // connect last node to head to make circle
        last->next = head;

        // circularily scroll the list
        auto new_tail = last;
        int steps = count - k;

        while (steps--) {
            new_tail = new_tail->next;
        }

        // set new head
        // cut linked list
        head = new_tail->next;
        new_tail->next = nullptr;
 
        return head;
    }
};