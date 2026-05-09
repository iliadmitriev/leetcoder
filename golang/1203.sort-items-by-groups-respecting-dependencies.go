func topologicalSort(graph [][]int, indegree []int) []int {
    n := len(graph)
    // init stack with nodes with 0 indegree
    visited := make([]int, 0, n) // len:0, cap:n
    // add to the starting stack state
    // all the nodes from graph with indegree equal to 0
    stack := make([]int, 0, n)
    for node := 0; node < n; node++ {
        if indegree[node] == 0 {
            stack = append(stack, node)
        }
    }

    for len(stack) > 0 {
        curr := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        visited = append(visited, curr)
        // iterate all the nodes adjacent to current with an edge
        for _, adj := range graph[curr] {
            // reduce their indegree (the current node is visited)
            indegree[adj]--;
            // if adjacent node indegee is equal to 0 (all its predecessor nodes visited)
            // then add it to stack
            if indegree[adj] == 0 {
                stack = append(stack, adj)
            }
        }
    }
    // if algorithm is able to visite all the nodes from graph
    // then there is no cycles, and nodes can be sorted topologically
    if len(visited) < n {
        return nil
    }
    return visited
}

func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
    // if item doesn't belong to any group assign it a new unique group id
    for i := 0; i < n; i++ {
        if group[i] == -1 {
            group[i] = m
            m++
        }
    }
    // init single items dependency graph and indegree of nodes
    item_graph := make([][]int, n)
    item_indegree := make([]int, n)
    // init item groups dependency graph and indegree of noodes
    group_graph := make([][]int, m)
    group_indegree := make([]int, m) 
    // build items and groups graph with their indegrees
    for curr := 0; curr < n; curr++ {
        for _, prev := range beforeItems[curr] {
            // each tuple (prev -> curr) is an edge in items graph
            item_graph[prev] = append(item_graph[prev], curr)
            item_indegree[curr]++
            // check if prev and curr belong to different groups
            // then add and edge in the group graph
            if group[curr] != group[prev] {
                group_graph[group[prev]] = append(group_graph[group[prev]], group[curr])
                group_indegree[group[curr]]++
            }
        }
    }
    // perform topological sort for group and items graph separately
    item_sorted := topologicalSort(item_graph, item_indegree)
    group_sorted := topologicalSort(group_graph, group_indegree)
    // if groups or items can't be sorted 
    // then return empty slice
    if item_sorted == nil || group_sorted == nil {
        return []int{}
    }

    // item are sorted regardless of groups
    // combine them to to groups they belong
    item_ordered_by_groups := make(map[int][]int)
    for _, item := range item_sorted {
        item_ordered_by_groups[group[item]] = append(item_ordered_by_groups[group[item]], item)
    }
    
    // concatenate all ordered_groups to result
    result := make([]int, 0, n)
    for _, group_id := range group_sorted {
        result = append(result, item_ordered_by_groups[group_id]...)
    }

    return result
} 