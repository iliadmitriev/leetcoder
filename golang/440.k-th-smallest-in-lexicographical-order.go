func findKthNumber(n int, k int) int {
	cur := 1 // pointer for current node
	i := 1   // step counter

	for i < k {
		numberOfChild := countChildNodes(cur, n)

		// if current node does not have enough children to cover the target
		if i+numberOfChild <= k {
			// then go to then right next node (brother)
			// and skip all then children nodes (at once)
			cur++
			i += numberOfChild
		} else {
			// otherwise go down to the next level with one step
			cur *= 10
			i++
		}
	}

	return cur
}

// countChildNodes: count number of child nodes between current node and its sibling.
// cur = 2, limit = 2500
// 2 .. 3 => 1
// 20 .. 30 => 10
// 200 .. 300 => 100
// 2000 .. 2501 => 501
// => 1 + 10 + 100 + 501 = 612
func countChildNodes(cur, limit int) int {
	count := 0

	// sibling node (will be used as a bound)
	bound := cur + 1

	for cur <= limit {

		count += bound - cur // add all the nodes in current level

		// go to the next level
		cur *= 10
		bound *= 10

		// bound is limited (not inclusive)
		if bound > limit+1 {
			bound = limit + 1
		}
	}

	return count
}
