const INIT_BUCKET_SIZE = int(1e6) / 8 + 1

type MyHashSet struct {
    // bit structure
    data [INIT_BUCKET_SIZE]byte
}

func Constructor() MyHashSet {
    return MyHashSet{}
}

func (this *MyHashSet) Add(key int)  {
    page := key / 8
    bit := key % 8
    this.data[page] |= 1 << bit
}


func (this *MyHashSet) Remove(key int)  {
    page := key / 8
    bit := key % 8
    this.data[page] &= ^(1 << bit)
}


func (this *MyHashSet) Contains(key int) bool {
    page := key / 8
    bit := key % 8
    return this.data[page] & (1 << bit) != 0
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */