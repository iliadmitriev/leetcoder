const Notes = int(5)

type ATM struct {
	storage []int
	notes   []int
}

func Constructor() ATM {
	return ATM{
		storage: make([]int, Notes),
		notes:   []int{20, 50, 100, 200, 500},
	}
}

func (this *ATM) Deposit(banknotesCount []int) {
	for i, v := range banknotesCount {
		this.storage[i] += v
	}
}

func (this *ATM) Withdraw(amount int) []int {
	res := make([]int, Notes)
	cur := make([]int, Notes)

	copy(cur, this.storage) // select for update

	for i := Notes - 1; i >= 0; i-- {

		count := amount / this.notes[i]
    rest := min(count, cur[i])

		cur[i] -= rest
		res[i] = rest
		amount -= this.notes[i] * rest
	}

	if amount != 0 {
		return []int{-1}
	}

	copy(this.storage, cur) // commit

	return res
}

/**
 * Your ATM object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Deposit(banknotesCount);
 * param_2 := obj.Withdraw(amount);
 */