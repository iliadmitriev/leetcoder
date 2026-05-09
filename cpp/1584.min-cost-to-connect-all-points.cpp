// calculate manhattan distance between two points
typedef vector<int> Point;

// absolute manhattan distance beetween p1 and p2
int dist(Point& p1, Point& p2) {
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]);
}

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        // result
        int mst = 0;
        int count = 0;
        // min priority qeueu of pairs(weight, node index)
        // S: O(n^2)
        typedef pair<int, int> tpl;
        std::priority_queue< tpl, vector<tpl>, std::greater<tpl> > pq;
        // add 0-th node with 0 weight
        pq.push(std::make_pair(0, 0));
        // visited nodes list S: O(n)
        std::vector<bool> seen(n, false);

        // T: O(n^2 * log n)
        while (count < n) {
            auto [weight, node] = pq.top(); pq.pop();

            if (seen[node]) {
                continue;
            }

            seen[node] = true;
            mst += weight;
            count++;

            for (int next_node = 0; next_node < n; next_node++) {
                if (!seen[next_node]) {
                    auto dis = dist(points[node], points[next_node]);
                    pq.push(make_pair(dis, next_node));
                }
            }
        }

        return mst;
    }
};