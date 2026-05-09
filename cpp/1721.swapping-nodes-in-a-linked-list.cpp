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
    ListNode* swapNodes(ListNode* head, int k) {
        // set dummy pointer to previos to head
        ListNode* res = new ListNode(0, head);

        // find first and pre first nodes
        ListNode* prev = res;
        ListNode* curr = res;
        for (; k && curr; k--) {
            prev = curr; curr = curr->next;
        }
        // save first and pre first nodes
        ListNode* first = curr;
        ListNode* pre_first = prev;

        // find second and pre second nodes
        ListNode* second = res;
        ListNode* pre_second = res;
        while (curr) {
            pre_second = second;
            second = second->next;
            curr = curr->next;
        }

        // make swaping
        swap(pre_first->next, pre_second->next);
        swap(first->next, second->next);

        // delete dummy node
        ListNode* ret = res->next;
        delete res;
        // return link to new result
        return ret;
    }
};