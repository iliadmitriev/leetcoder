type MyQueue struct {
    input, output []int
}


func Constructor() MyQueue {
    return MyQueue{
        make([]int, 0),
        make([]int, 0),
    }
}

// move - fill output from input with O(n)
// if output is empty
func (this *MyQueue) move() {
    if len(this.output) > 0 {
        return
    }

    for len(this.input) > 0 {
        n := len(this.input)
        x := this.input[n - 1]
        this.input = this.input[:n - 1]

        this.output = append(this.output, x)
    }
}


func (this *MyQueue) Push(x int)  {
    this.input = append(this.input, x)
}


func (this *MyQueue) Pop() int {
    this.move()
    n := len(this.output)
    x := this.output[n - 1]
    this.output = this.output[:n - 1]
    return x
}


func (this *MyQueue) Peek() int {
    this.move()
    n := len(this.output)
    return this.output[n - 1]
}


func (this *MyQueue) Empty() bool {
    return len(this.input) == 0 && len(this.output) == 0
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */