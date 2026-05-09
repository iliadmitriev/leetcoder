#include <vector>

using std::vector;

class Solution {
public:
  vector<int> nodesBetweenCriticalPoints(ListNode *head) {
    if (!head || !head->next)
      return {-1, -1};

    int firstIdx = -1, prevIdx = -1, minDist = -1, maxDist = -1;

    ListNode *prev = head, *curr = head->next, *next = head->next->next;
    int i = 1;
    while (next) {

      if ((prev->val > curr->val && curr->val < next->val) ||
          (prev->val < curr->val && curr->val > next->val)) {

        if (firstIdx == -1) {
          firstIdx = i;
        } else {
          maxDist = i - firstIdx;
          if (minDist == -1)
            minDist = maxDist;
          minDist = std::min(minDist, i - prevIdx);
        }

        prevIdx = i;
      }

      prev = curr;
      curr = next;
      next = next->next;
      i++;
    }

    return {minDist, maxDist};
  }
};