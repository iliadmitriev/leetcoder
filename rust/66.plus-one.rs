impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        let mut carry = 1;

        for digit in digits.iter_mut().rev() {
            let sum = carry + *digit;
            *digit = sum % 10;
            carry = sum / 10;

            if carry == 0 {
                break;
            }
        }

        if carry > 0 {
            digits.insert(0, 1);
        }

        digits
    }
}