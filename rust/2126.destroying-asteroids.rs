impl Solution {
    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>) -> bool {
        let mut asteroids = asteroids;
        let mut mass = mass as i64;

        asteroids.sort_unstable();

        for ast in asteroids.iter().map(|&x| x as i64) {
            if mass < ast {
                return false;
            }

            mass += ast;
        }

        true
    }
}
