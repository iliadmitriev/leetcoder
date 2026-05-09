/**
 * Definition for singly-linked list.
 */
#include <unordered_set>
#include <vector>

using namespace std;

// struct ListNode {
//   int val;
//   ListNode *next;
//   ListNode() : val(0), next(nullptr) {}
//   ListNode(int x) : val(x), next(nullptr) {}
//   ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

class Solution {
public:
  int numComponents(ListNode *head, vector<int> &nums) {
    if (!head) {
      return 0;
    }

    unordered_set<int> num_set(nums.begin(), nums.end());

    int res = nums.size();
    ListNode *prev = head;
    head = head->next;

    while (head) {
      if (num_set.find(prev->val) != num_set.end() &&
          num_set.find(head->val) != num_set.end()) {
        res--;
      }

      prev = head;
      head = head->next;
    }

    return res;
  }
};