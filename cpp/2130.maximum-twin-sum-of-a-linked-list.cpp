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
private:
    // return middle of linked list
    ListNode* findMid(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    // reverse linked list
    ListNode* revList(ListNode* head) {
        ListNode* pre = NULL;
        ListNode* cur = head;
        ListNode* nxt = NULL;

        while (cur) {
            // save next pointer
            nxt = cur->next;

            // link current to previous
            cur->next = pre;

            // move forward both pointers
            pre = cur;
            cur = nxt;
        }

        return pre;
    }

public:
    int pairSum(ListNode* head) {
        ListNode* mid = findMid(head);
        ListNode* second = revList(mid);

        int maxRes = 0;
        while (head && second) {
            maxRes = max(maxRes, head->val + second->val);
            head = head->next;
            second = second->next;
        }
        return maxRes;
    }
};