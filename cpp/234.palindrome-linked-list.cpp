// struct ListNode {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
  bool isPalindrome(ListNode *head) {
    if (head == nullptr || head->next == nullptr) {
      return true;
    }

    // reverse first half of linked list up to the middle
    ListNode *slow = head, *fast = head, *prev = nullptr, *tmp = nullptr;
    while (slow && fast && fast->next) {
      tmp = slow;

      slow = slow->next;
      fast = fast->next->next;

      tmp->next = prev;
      prev = tmp;
    }

    // if number of nodes is odd, skip the middle node
    if (fast) {
      slow = slow->next;
    }

    // compare first reversed half and second half
    while (slow && prev && slow->val == prev->val) {
      slow = slow->next;
      prev = prev->next;
    }

    return !prev;
  }
};