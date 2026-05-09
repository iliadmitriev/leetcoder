func unique[K comparable](slice []K) []K {
    m := make(map[K]bool)
    unq := make([]K, 0, len(slice))
    for _, val := range slice {
        if !m[val] {
            m[val] = true
            unq = append(unq, val)
        }
    }
    return unq
}

func get_count[K comparable](slice []K, value K) (res int) {
    for _, val := range slice {
        if val == value {
            res++
        }
    }
    return
}

func get_roads_count(roads [][]int, degrees []int, city1 int, city2 int) (res int) {
    for _, road := range roads{
        if (degrees[road[0]] == city1 && degrees[road[1]] == city2) ||
            (degrees[road[0]] == city2 && degrees[road[1]] == city1) {
                res++
            }
    }
    return
}

func maximalNetworkRank(n int, roads [][]int) int {
    degrees := make([]int, n)

    for _, road := range roads {
        u, v := road[0], road[1]        
        degrees[u]++
        degrees[v]++
    }

    // get unique values from degrees
    // sorted descending
    uniqueDegrees := unique(degrees)
    sort.Sort(sort.Reverse(sort.IntSlice(uniqueDegrees)))

    // get first and second largest degree
    first := uniqueDegrees[0]
    second := 0
    if len(uniqueDegrees) > 1 {
        second = uniqueDegrees[1]
    }

    // get count of first and second degrees
    first_count, second_count := get_count(degrees, first), get_count(degrees, second)

    // if there is many cities with max degrees
    if first_count > 1 {
        connected_count := get_roads_count(roads, degrees, first, first)
        possible_count := first_count * (first_count - 1) / 2
        if connected_count == possible_count {
            return first + first - 1
        }
        return first + first
    }

    first_to_second_count := get_roads_count(roads, degrees, first, second)
    if first_to_second_count == second_count {
        return first + second - 1
    }
    return first + second
}