impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let mut collisions = 0;

        let to_int = |c| match c {
            'L' => -1,
            'R' => 1,
            _ => 0,
        };

        let mut st = Vec::with_capacity(directions.len());

        for d in directions.chars() {
            let mut dd = to_int(d);

            while !st.is_empty() && *st.last().unwrap() > dd {
                let vv = st.pop().unwrap();
                collisions += vv - dd;
                dd = 0;
            }

            st.push(dd);
        }

        return collisions;
    }
}