type RecentCounter struct {
    que []int
}


func Constructor() RecentCounter {
    return RecentCounter{
        que: []int{},
    }
}


func (this *RecentCounter) Ping(t int) int {
    this.que = append(this.que, t)

    for this.que[0] < t - 3000 {
        this.que = this.que[1:]
    }

    return len(this.que)
}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */