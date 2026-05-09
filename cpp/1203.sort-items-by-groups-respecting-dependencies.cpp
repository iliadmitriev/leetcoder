class Solution {
private:
    vector<int> topological_sort(vector<vector<int>>& graph, vector<int>& indegree) {
        vector<int> visited;
        // init stack with nodes with 0 indegree
        stack<int> stack;
        // add to the starting stack state
        // all the nodes from graph with indegree equal to 0
        for (int node = 0; node < graph.size(); node++)
            if (indegree[node] == 0)
                stack.push(node);

        while (!stack.empty()) {
            auto curr = stack.top(); stack.pop();
            visited.push_back(curr);
            // iterate all the nodes adjacent to current with an edge
            for (auto adj : graph[curr]) {
                // reduce their indegree (the current node is visited)
                indegree[adj]--;
                // if adjacent node indegee is equal to 0 (all its predecessor nodes visited)
                // then add it to stack
                if (indegree[adj] == 0)
                    stack.push(adj);
            }

        }
        // if algorithm is able to visite all the nodes from graph
        // then there is no cycles, and nodes can be sorted topologically
        return visited.size() == graph.size()
            ? visited
            : vector<int>{};
    }

public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        // if item doesn't belong to any group assign it an unique group id
        for (int i = 0; i < n; i++)
            if (group[i] == -1) {
                group[i] = m;
                m++;
            }

        // init single items dependency graph and indegree of nodes
        vector<vector<int>> item_graph(n, vector<int>());
        vector<int> item_indegree(n, 0);

        // init item groups dependency graph and indegree of noodes 
        vector<vector<int>> group_graph(m, vector<int>());
        vector<int> group_indegree(m, 0);


        // build items and groups graph with their indegrees
        for (int curr = 0; curr < n; curr++)
            for (auto prev : beforeItems[curr]) {
                // each tuple (prev -> curr) is an edge in items graph
                item_graph[prev].push_back(curr);
                item_indegree[curr]++;

                // check if prev and curr belong to different groups
                // then add and edge in the group graph
                if (group[curr] != group[prev]) {
                    group_graph[group[prev]].push_back(group[curr]);
                    group_indegree[group[curr]]++;
                }

            }

        // perform topological sort for group and items graph separately
        vector<int> item_sorted = topological_sort(item_graph, item_indegree);
        vector<int> group_sorted = topological_sort(group_graph, group_indegree);

        if (item_sorted.empty() || group_sorted.empty())
            return vector<int>{};

        // item are sorted regardless of groups
        // combine them to to groups they belong
        map<int, vector<int>> item_ordered_by_groups;
        for (auto item : item_sorted) {
            item_ordered_by_groups[group[item]].push_back(item);
        }

        // concatenate all ordered_groups to result
        vector<int> result = {};

        for (auto group_idx : group_sorted)
            result.insert(
                result.end(),
                item_ordered_by_groups[group_idx].begin(),
                item_ordered_by_groups[group_idx].end()
            );
        
        return result;
    }
};