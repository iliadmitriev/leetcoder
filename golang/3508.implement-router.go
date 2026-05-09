type packet [3]int

type Router struct {
	limit   int
	q       []packet            // queue of packets
	cache   map[packet]struct{} // cache of uniq packets
	counter map[int][]int       // counters of destination -> slice of ordered time
}

func Constructor(memoryLimit int) Router {
	return Router{
		limit:   memoryLimit,
		q:       make([]packet, 0, memoryLimit),
		cache:   make(map[packet]struct{}),
		counter: make(map[int][]int),
	}
}

func (this *Router) AddPacket(source int, destination int, timestamp int) bool {
	pack := packet{source, destination, timestamp}

	if _, ok := this.cache[pack]; ok {
		return false
	}

	// pop packet if queue is full
	if len(this.q) == this.limit {
		this.pop()
	}

	// add packet
	this.q = append(this.q, pack)
	this.cache[pack] = struct{}{}
	this.incCounter(pack)

	return true
}

func (this *Router) ForwardPacket() []int {
	if len(this.q) == 0 {
		return []int{}
	}

	pack := this.pop()

	return []int{pack[0], pack[1], pack[2]}
}

func (this *Router) GetCount(destination int, startTime int, endTime int) int {
	dest := this.counter[destination]

	left := this.bisectLeft(dest, startTime)
	right := this.bisectRight(dest, endTime)

	return right - left
}

func (this *Router) pop() packet {
	pack := this.q[0]
	this.q = this.q[1:]
	this.decCounter(pack)
	delete(this.cache, pack)

	return pack
}

func (this *Router) incCounter(pack packet) {
	dest, tm := pack[1], pack[2]

	this.counter[dest] = append(this.counter[dest], tm)
}

func (this *Router) decCounter(pack packet) {
	dest, tm := pack[1], pack[2]

	counter := this.counter[dest]
	left := this.bisectLeft(counter, tm)

	if left < len(counter) && counter[left] == tm {
		left++
	}

	this.counter[dest] = counter[left:] // memory leak
}

func (this *Router) bisectLeft(arr []int, target int) int {
	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] < target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return lo
}

func (this *Router) bisectRight(arr []int, target int) int {
	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if target < arr[mid] {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}

/**
 * Your Router object will be instantiated and called as such:
 * obj := Constructor(memoryLimit);
 * param_1 := obj.AddPacket(source,destination,timestamp);
 * param_2 := obj.ForwardPacket();
 * param_3 := obj.GetCount(destination,startTime,endTime);
 */