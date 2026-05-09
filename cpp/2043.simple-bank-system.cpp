#include <vector>
using std::vector;

class Bank {
private:
  vector<long long> accounts;

  inline bool valid(int account) {
    return 0 <= account && account < accounts.size();
  }

  inline bool enough(int account, long long money) {
    return accounts[account] >= money;
  }

public:
  Bank(vector<long long> &balance) : accounts(std::move(balance)) {}

  bool transfer(int account1, int account2, long long money) {
    account1--;
    account2--;

    if (!valid(account1) || !valid(account2) || !enough(account1, money)) {
      return false;
    }

    accounts[account1] -= money;
    accounts[account2] += money;
    return true;
  }

  bool deposit(int account, long long money) {
    account--;

    if (!valid(account)) {
      return false;
    }

    accounts[account] += money;
    return true;
  }

  bool withdraw(int account, long long money) {
    account--;

    if (!valid(account) || !enough(account, money)) {
      return false;
    }

    accounts[account] -= money;
    return true;
  }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */