type CustomStack struct {
	top, cap  int
	data, inc []int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{
		0, maxSize, make([]int, maxSize), make([]int, maxSize),
	}
}

func (this *CustomStack) Push(x int) {
	if this.top == this.cap {
		return
	}

	this.data[this.top] = x
	this.inc[this.top] = 0

	this.top++
}

func (this *CustomStack) Pop() int {
	if this.top == 0 {
		return -1
	}

	this.top--
	x := this.data[this.top] + this.inc[this.top]

	if this.top > 0 {
		this.inc[this.top-1] += this.inc[this.top]
	}

	return x
}

func (this *CustomStack) Increment(k int, val int) {
	k = min(k-1, this.top-1)
	if k >= 0 {
		this.inc[k] += val
	}
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */