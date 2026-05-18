// IntQueue is a typed FIFO queue backed by a slice
type IntQueue struct {
	data []int
}

// NewWithCapacity creates a new IntQueue with pre-allocated capacity
func NewWithCapacity(capacity int) *IntQueue {
	return &IntQueue{data: make([]int, 0, capacity)}
}

// PushBack adds an element to the end of the queue
func (q *IntQueue) PushBack(val int) {
	q.data = append(q.data, val)
}

// PopFront removes and returns the front element of the queue
func (q *IntQueue) PopFront() int {
	val := q.data[0]
	q.data = q.data[1:] // O(1) slice reslicing
	return val
}

// Len returns the number of elements in the queue
func (q *IntQueue) Len() int {
	return len(q.data)
}

// IsEmpty checks if the queue contains no elements
func (q *IntQueue) IsEmpty() bool {
	return len(q.data) == 0
}

func minJumps(arr []int) int {
	n := len(arr)
	if n <= 1 {
		return 0
	}

	// Build adjacency map: value -> list of indices
	adj := make(map[int][]int)
	for i, v := range arr {
		adj[v] = append(adj[v], i)
	}

	seen := make([]bool, n)
	queue := NewWithCapacity(n)
	queue.PushBack(0)
	seen[0] = true
	step := 0

	for !queue.IsEmpty() {
		for range queue.Len() {
			curr := queue.PopFront()

			// Reached the target
			if curr == n-1 {
				return step
			}

			// Jump to i + 1
			if curr+1 < n && !seen[curr+1] {
				seen[curr+1] = true
				queue.PushBack(curr + 1)
			}

			// Jump to i - 1
			if curr-1 >= 0 && !seen[curr-1] {
				seen[curr-1] = true
				queue.PushBack(curr - 1)
			}

			// Jump to all indices with the same value
			if indices, ok := adj[arr[curr]]; ok {
				for _, j := range indices {
					if !seen[j] {
						seen[j] = true
						queue.PushBack(j)
					}
				}
				// CRITICAL OPTIMIZATION:
				// Remove the key after first use. Without this, arrays with
				// many duplicates cause O(N^2) behavior.
				delete(adj, arr[curr])
			}
		}
		step++
	}

	return step
}