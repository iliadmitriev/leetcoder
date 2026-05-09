impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut count = 0;

        for i in 1..=n {
            for j in i..=n {
                let v = i * i + j * j;
                let r = (v as f64).sqrt() as i32;

                if r > n {
                    break;
                }

                if r * r == v {
                    count += 2;
                }
            }
        }

        count
    }
}