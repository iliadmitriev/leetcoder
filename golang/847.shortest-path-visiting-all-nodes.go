// Idea:

//     BFS simultaneosly from all the nodes,
//     marking all visited nodes.
//     BFS garantees than first finished node is the minimal path.

// Algorithm:

//     1. add all nodes with their mask to queue as start nodes with 0 distance
//         (mask with only one bit set)
//     2. queue:
//         2.1. get current node, it's mask and distance from queue
//         2.2. if mask is all set to 1's then all nodes visited,
//             so return distance
//         2.3. iterate all neighbour nodes from current node
//             2.3.1. check if node is not visited with current mask
//             2.3.2. add node to visited, and add to queue with it's new mask, and new distance + 1

// Complexity:

//     For every starting node (n) there is 2^n combination (2 because visited or not):

//     Time: O(n * 2^n)
//     Space: O(n * 2^n)

func shortestPathLength(graph [][]int) int {
    n := len(graph)
    queue := make([][3]int, 0, n * (1 << n))
    finish := (1 << n) - 1

    cache := make([][]bool, 1<<n)
	for i := range cache {
		cache[i] = make([]bool, n)
	}


    for node := 0; node < n; node++ {
        cache[1 << node][node] = false // node, mask
        queue = append(queue, [3]int{node, 1 << node, 0}) // node, mask, distance
    }

    for len(queue) > 0 {
        // pop new node from queue
        node := queue[0]
        queue = queue[1:len(queue)]

        if node[1] == finish {
            return node[2]
        }

        for _, adj := range graph[node[0]] {
            newMask := node[1] | (1 << adj)

            // it's already calculated
            if cache[newMask][adj] {
                continue
            }

            cache[newMask][adj] = true
            queue = append(queue, [3]int{adj, newMask, node[2] + 1})
        }
    }

    return -1
}