type MyStack struct {
    q []int
}


func Constructor() MyStack {
    return MyStack{}
}


func (this *MyStack) Push(x int)  {
    this.q = append(this.q, x)
    for j := 0; j < len(this.q) - 1; j++ {
        this.q = append(this.q, this.q[0])
        this.q = this.q[1:]
    }
}


func (this *MyStack) Pop() int {
    x := this.q[0]
    this.q = this.q[1:]
    return x
}


func (this *MyStack) Top() int {
    return this.q[0]
}


func (this *MyStack) Empty() bool {
    return len(this.q) == 0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */