
class Solution {
public:
  ListNode *doubleIt(ListNode *head) {

    function<tuple<ListNode *, bool>(ListNode *)> dfs;
    dfs = [&](ListNode *node) -> tuple<ListNode *, int> {
      if (!node)
        return {nullptr, 0};

      auto [res, carry] = dfs(node->next);

      node->val = 2 * node->val + carry;
      carry = node->val / 10;
      node->val %= 10;
      node->next = res;

      return {node, carry};
    };

    auto [res, carry] = dfs(head);
    if (carry) {
      res = new ListNode(1, res);
    }

    return res;
  }
};