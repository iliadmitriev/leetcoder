impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        let total = nums.iter().sum();
        
        if total % 3 == 0 {
            return total;
        }

        let mut a1 = 1_000_000_000;
        let mut b1 = 1_000_000_000;
        let mut a2 = 1_000_000_000;
        let mut b2 = 1_000_000_000;

        for num in nums {
            if num % 3 == 1 {
                if num <= a1 {
                    b1 = a1;
                    a1 = num;
                } else if num < b1 {
                    b1 = num;
                }
            }

            if num % 3 == 2 {
                if num <= a2 {
                    b2 = a2;
                    a2 = num;
                } else if num < b2 {
                    b2 = num;
                }
            }
        }

        if total % 3 == 1 {
            return total - std::cmp::min(a1, a2 + b2);
        }

        total - std::cmp::min(a1 + b1, a2)
    }
}