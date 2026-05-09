func eliminateMaximum(dist []int, speed []int) int {
    n := len(dist)
    // count number of monsters arrived at every minute
    arrived := make([]int, n)
    for i := 0; i < n; i++ {
        // divide distance to speed
        // ceil rount using remainder
        num := dist[i] / speed[i]
        r := dist[i] % speed[i]
        if r != 0 {
            num++
        }
        // check bounds
        if num < n {
            arrived[num]++
        }
    }


    for i := 1; i < len(arrived); i++ {
        // accumulate with previous arrived monsters
        arrived[i] += arrived[i - 1]
        // if at any moment in time count of monsters arrived
        // more than can be killed 
        if arrived[i] > i {
            return i
        }
    }
    return n
}