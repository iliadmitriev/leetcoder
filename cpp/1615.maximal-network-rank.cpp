class Solution {
private:
    int get_count_by_degree(vector<vector<int>>& roads, vector<int>& degrees, int a, int b) {
        int res = 0;
        for (const auto& road : roads) 
            if (
                    (degrees[road[0]] == a && degrees[road[1]] == b)
                    || (degrees[road[0]] == b && degrees[road[1]] == a)
                ) res++;
        return res;
    }

public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> degree(n, 0);
        for (const auto& road : roads) {
            degree[road[0]]++; degree[road[1]]++;
        }

        unordered_set<int> unique_degrees(degree.begin(), degree.end());
        vector<int> sorted_degrees(unique_degrees.begin(), unique_degrees.end());
        std::sort(sorted_degrees.rbegin(), sorted_degrees.rend());

        int first = sorted_degrees[0];
        int second = sorted_degrees.size() > 1 ? sorted_degrees[1] : 0;

        int first_count = std::count(degree.begin(), degree.end(), first);
        int second_count = std::count(degree.begin(), degree.end(), second);

        // if there is multiple cities have max degree
        if (first_count > 1) {
            int connected_count = get_count_by_degree(roads, degree, first, first);
            int possible_connected_count = first_count * (first_count - 1) / 2;
            int rank = first + first;
            return connected_count == possible_connected_count
                ? rank - 1
                : rank ;

        }
        
        int first_to_second_conn_count = get_count_by_degree(roads, degree, first, second);
        int rank = first + second;
        return first_to_second_conn_count == second_count
            ? rank - 1
            : rank ;
    }
};