const (
  MOD = int(1e9) + 7
)

type Fancy struct {
   data []int
   w []int
   b []int
   last int
}


func Constructor() Fancy {
    return Fancy{
      data: []int{},
      w: []int{1},
      b: []int{0},
      last: 0,
    }
}


func (this *Fancy) Append(val int)  {
    this.data = append(this.data, val)
    this.w = append(this.w, this.w[this.last])
    this.b = append(this.b, this.b[this.last])
    this.last++
}


func (this *Fancy) AddAll(inc int)  {
  this.b[this.last] = (this.b[this.last] + inc) % MOD
}


func (this *Fancy) MultAll(m int)  {
  this.w[this.last] = (this.w[this.last] * m) % MOD
  this.b[this.last] = (this.b[this.last] * m) % MOD
}


func (this *Fancy) GetIndex(idx int) int {
  if idx >= len(this.data) {
    return -1
  }

  wo := (this.inv(this.w[idx]) * this.w[this.last]) % MOD
  bo := (this.b[this.last] - this.b[idx] * wo % MOD + MOD) % MOD

  return (wo * this.data[idx] % MOD + bo) % MOD
}

// multiplicative modular inverse (MOD) returns (1 / x) % MOD 
func (this *Fancy) inv(x int) int {
  return this.exp(x, MOD - 2)
}

// modular exponent returns (x ^ y) % MOD
func (this *Fancy) exp(x, y int) int {
  ret := 1

  for cur := x; y != 0; y >>= 1 {
    if y & 1 == 1 {
      ret = (ret * cur) % MOD
    }

    cur = (cur * cur) % MOD
  }

  return ret
}


/**
 * Your Fancy object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * param_4 := obj.GetIndex(idx);
 */