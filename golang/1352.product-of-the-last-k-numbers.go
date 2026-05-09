type ProductOfNumbers struct {
	nums []int
}

func Constructor() ProductOfNumbers {
	return ProductOfNumbers{
		nums: []int{1},
	}
}

func (this *ProductOfNumbers) Add(num int) {
	n := len(this.nums)

	if num == 0 {
		this.nums = this.nums[:0]
		this.nums = append(this.nums, 1)
		return
	}

	this.nums = append(this.nums, this.nums[n-1]*num)
}

func (this *ProductOfNumbers) GetProduct(k int) int {
	n := len(this.nums)

	if k >= n {
		return 0
	}

	return this.nums[n-1] / this.nums[n-k-1]
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */