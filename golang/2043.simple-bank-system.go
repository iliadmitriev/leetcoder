
type Bank struct {
	accounts []int64
}

func Constructor(balance []int64) Bank {
	n := len(balance)
	acc := make([]int64, n+1)

	for i := range n {
		acc[i+1] = balance[i]
	}

	return Bank{
		accounts: acc,
	}
}

func (this *Bank) checkAcc(id int) bool {
	if 0 >= id || id >= len(this.accounts) {
		return false
	}

	return true
}

func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
	if !this.checkAcc(account1) || !this.checkAcc(account2) {
		return false
	}

	cur1 := this.accounts[account1]
	if cur1 < money {
		return false
	}

	this.accounts[account1] -= money
	this.accounts[account2] += money
	return true
}

func (this *Bank) Deposit(account int, money int64) bool {
	if !this.checkAcc(account) {
		return false
	}

	this.accounts[account] += money
	return true
}

func (this *Bank) Withdraw(account int, money int64) bool {
	if !this.checkAcc(account) {
		return false
	}

	cur := this.accounts[account]
	if cur < money {
		return false
	}

	this.accounts[account] -= money
	return true
}

/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */