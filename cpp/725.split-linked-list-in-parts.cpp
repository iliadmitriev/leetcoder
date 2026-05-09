
class Solution {
public:
  vector<ListNode *> splitListToParts(ListNode *head, int k) {

    int len = 0;

    for (auto ptr = head; ptr != nullptr; ptr = ptr->next) {
      len++;
    }

    int full = len / k, extra = len % k;

    ListNode *prev = nullptr;

    vector<ListNode *> parts(k, nullptr);

    for (int i = 0; i < k; i++) {
      // set chunk start pointer
      parts[i] = head;

      // calculate number of nodes in current chunk
      // and iterate through them
      int size = full + (i < extra ? 1 : 0);
      for (; size > 0; size--) {
        prev = head;
        head = head->next;
      }

      // cut chunk at the ending node
      if (prev) {
        prev->next = nullptr;
      }
    }

    return parts;
  }
};