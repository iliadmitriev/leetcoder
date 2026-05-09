func closestMeetingNode(edges []int, node1 int, node2 int) int {
	vis1, vis2 := make([]bool, len(edges)), make([]bool, len(edges))
	proceed := true

	for proceed {
		vis1[node1] = true
		vis2[node2] = true

		switch {
		case vis1[node2] && vis2[node1]:
			return min(node1, node2)
		case vis1[node2]:
			return node2
		case vis2[node1]:
			return node1
		}

		proceed = false

		if edges[node1] != -1 && !vis1[edges[node1]] {
			node1 = edges[node1]
			proceed = true
		}

		if edges[node2] != -1 && !vis2[edges[node2]] {
			node2 = edges[node2]
			proceed = true
		}
	}

	return -1
}
