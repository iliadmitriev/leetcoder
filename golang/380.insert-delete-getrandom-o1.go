import (
  "math/rand"
)

type RandomizedSet struct {
	data    []int
	indices map[int]int
}

func Constructor() RandomizedSet {
  return RandomizedSet{
    data: make([]int, 0),
    indices: make(map[int]int),
  }
}

func (this *RandomizedSet) Insert(val int) bool {
  if _, ok := this.indices[val]; ok {
    return false
  }

  last := len(this.data)
  this.indices[val] = last
  this.data = append(this.data, val)
  return true
}

func (this *RandomizedSet) Remove(val int) bool {
  if _, ok := this.indices[val]; !ok {
    return false
  }

  lastIdx := len(this.data) - 1
  lastVal := this.data[lastIdx]

  idx := this.indices[val]
  this.data[idx] = lastVal
  this.indices[lastVal] = idx

  this.data = this.data[:lastIdx]
  delete(this.indices, val)
  return true
}

func (this *RandomizedSet) GetRandom() int {
  idx := rand.Intn(len(this.data))
  return this.data[idx]
}
