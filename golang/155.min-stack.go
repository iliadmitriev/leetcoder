type MinStack struct {
	st [][2]int // 0: value, 1: current min
}

func Constructor() MinStack {
	return MinStack{
		st: [][2]int{},
	}
}

func (this *MinStack) Push(val int) {
	var mi int
	n := len(this.st)
	if n == 0 {
		mi = val
	} else {
		mi = this.st[n-1][1]
	}

	mi = min(mi, val)
	this.st = append(this.st, [2]int{val, mi})
}

func (this *MinStack) Pop() {
	this.st = this.st[:len(this.st)-1]
}

func (this *MinStack) Top() int {
	return this.st[len(this.st)-1][0]
}

func (this *MinStack) GetMin() int {
	return this.st[len(this.st)-1][1]
}
