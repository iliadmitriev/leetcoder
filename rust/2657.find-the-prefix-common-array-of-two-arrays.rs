impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let N = a.len();

        let mut cache = vec![0; N + 1]; // starts from 0
        let mut res = vec![0; N];
        let mut cur = 0; // current count

        for (i, (&va, &vb)) in a.iter().zip(b.iter()).enumerate() {
            let i1 = va as usize;
            let i2 = vb as usize;

            cache[i1] += 1;
            if (cache[i1] == 2) {
                cur += 1;
            }

            cache[i2] += 1;
            if (cache[i2] == 2) {
                cur += 1;
            }

            res[i] = cur;
        }

        res
    }
}
