#include <algorithm>
#include <vector>

using std::vector;

struct Node {
    // Maximum distance between any two consecutive obstacles within a node
    // range. Primary metrice to answer the question is the block of size "sz"
    // can fit.
    int max_gap;

    // The leftmost obstacle coordinate in this range.
    // For gap calculation on merge operation
    int l_pos;

    // The rightmost obstacle coordinate.
    // For gap calculation on merge operation
    int r_pos;

    // True if the range contains at least one obstacle
    // For empty of leaf nodes calculations
    bool has_obstacle;

    static Node merge(const Node& L, const Node& R) {
        Node res;

        res.has_obstacle = L.has_obstacle || R.has_obstacle;

        res.l_pos = L.has_obstacle ? L.l_pos : R.l_pos;
        res.r_pos = R.has_obstacle ? R.r_pos : L.r_pos;


        res.max_gap = std::max(L.max_gap, R.max_gap);

        if (L.has_obstacle && R.has_obstacle) {
            res.max_gap = std::max(res.max_gap, R.l_pos - L.r_pos);
        }

        return res;
    }
};

class SegmentTree {
private:
    vector<Node> tree;
    vector<int> coords;
    int n;

    // Place obstacle at index idx and propagate recursively changes to the tree
    // node - current node
    // start, end - range of indices covered by this node (inclusive)
    // idx - index where the new obstacle is placed
    void update(int node, int start, int end, int idx) {
        if (start == end) {
            tree[node] = Node{
                .max_gap = 0,
                .l_pos = coords[start],
                .r_pos = coords[end],
                .has_obstacle = true,
            };

            return;
        }

        const int mid = start + (end - start) / 2;
        const int left = node << 1;
        const int right = (node << 1) | 1;

        if (idx <= mid) {
            update(left, start, mid, idx);
        } else {
            update(right, mid + 1, end, idx);
        }

        tree[node] = Node::merge(tree[left], tree[right]);
    }

    // Query and recursively aggregate for a specific range
    // node - current tree node
    // start, end - range of indices covered byt this node (inclusive)
    // l, r - query coordinate range
    Node query(int node, int start, int end, int l, int r) const {
        if (r < start || end < l) {
            return Node{
                .max_gap = 0,
                .l_pos = 0,
                .r_pos = 0,
                .has_obstacle = false,
            };
        }

        if (l <= start && end <= r) {
            return tree[node];
        }

        const int mid = start + (end - start) / 2;
        const int left = node << 1;
        const int right = (node << 1) | 1;

        Node left_res = query(left, start, mid, l, r);
        Node right_res = query(right, mid + 1, end, l, r);

        if (!left_res.has_obstacle) {
            return right_res;
        }

        if (!right_res.has_obstacle) {
            return left_res;
        }

        return Node::merge(left_res, right_res);
    }

public:
    SegmentTree(const vector<int>& coordinates)
        : coords(coordinates), n(coordinates.size()) {
        tree.assign(4 * n, Node{0, 0, 0, false});
        update(1, 0, n - 1, 0);
    }

    void addObstacle(int idx) { update(1, 0, n - 1, idx); }

    [[nodiscard]] Node queryRange(int left, int right) {
        return query(1, 0, n - 1, left, right);
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        // collect all sorted and unique x coords
        vector<int> coords;
        coords.reserve(queries.size() + 1);
        coords.push_back(0);
        for (const auto& q : queries) {
            coords.push_back(q[1]);
        }

        std::ranges::sort(coords);
        auto [dup_start, dup_end] = std::ranges::unique(coords);
        coords.erase(dup_start, dup_end);

        SegmentTree tree(coords);
        vector<bool> results;
        results.reserve(queries.size());

            for (const auto& q : queries) {
            if (q[0] == 1) {
                const int x = q[1];
                const int idx =
                    std::ranges::lower_bound(coords, x) - coords.begin();

                tree.addObstacle(idx);
            } else {
                const int x = q[1], sz = q[2];
                const int idx =
                    std::ranges::lower_bound(coords, x) - coords.begin();

                Node res = tree.queryRange(0, idx);
                int right_gap = x - res.r_pos;
                int max_space = res.max_gap;

                max_space = std::max(max_space, right_gap);

                results.push_back(max_space >= sz);
            }
        }

        return results;
    }
};