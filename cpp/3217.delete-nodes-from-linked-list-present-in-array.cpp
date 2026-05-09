class Solution {
public:
  ListNode *modifiedList(vector<int> &nums, ListNode *head) {
    ListNode *res = new ListNode();
    ListNode *ptr = res;

    unordered_set<int> toRemove(nums.begin(), nums.end());

    while (head) {
      if (!toRemove.count(head->val)) {
        ptr->next = head;
        ptr = ptr->next;
        head = head->next;
      } else {
        ListNode *tmp = head;
        head = head->next;
        delete tmp;
      }
    }

    ptr->next = nullptr;

    while (head) {
      ListNode *tmp = head;
      head = head->next;
      delete tmp;
    }

    ListNode *ans = res->next;
    delete res;
    return ans;
  }
};