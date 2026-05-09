
type BinaryIndexTree struct {
	tree []int
}

func NewBinaryIndexTree(n int) BinaryIndexTree {
	return BinaryIndexTree{tree: make([]int, n+1)}
}

func (t *BinaryIndexTree) Update(index int, val int) {
	index++
	for index < len(t.tree) {
		t.tree[index] += val
		index += index & -index
	}
}

func (t *BinaryIndexTree) SumRange(index int) int {
	res := 0
	index++

	for index > 0 {
		res += t.tree[index]
		index -= index & -index
	}
	return res
}

type NumArray struct {
	nums []int
	bits BinaryIndexTree
}

func Constructor(nums []int) NumArray {
	bits := NewBinaryIndexTree(len(nums))
	for i, num := range nums {
		bits.Update(i, num)
	}

	return NumArray{nums: nums, bits: bits}
}

func (this *NumArray) Update(index int, val int) {
	delta := val - this.nums[index]
	this.nums[index] = val
	this.bits.Update(index, delta)
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.bits.SumRange(right) - this.bits.SumRange(left-1)
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */