func numBusesToDestination(routes [][]int, source int, target int) int {
    // no need to take a bus
    if source == target {
        return 0
    }

    gr := make(map[int][]int)
    stops := 0
    for bus, route := range routes {
        for _, stop := range route {
            gr[stop] = append(gr[stop], bus)
            stops++
        }
    }
    // prelimirary check: if source or target are not on any bus line
    // then it's impossible to get from source to target
    if len(gr[source]) == 0 || len(gr[target]) == 0 {
        return -1
    }

    // queue of tuples (stop, distance)
    // with reserve capacity number of stops
    q := make([][2]int, 0, stops)
    q = append(q, [2]int{source, 0})
    // visited buses and visited stops
    vis_stops := make(map[int]bool)
    vis_buses := make([]bool, len(routes))

    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        stop, dist := node[0], node[1]

        if stop == target {
            return dist
        }

        for _, bus := range gr[stop] {
            if vis_buses[bus] {
                continue
            }
            vis_buses[bus] = true

            for _, next_stop := range routes[bus] {
                if vis_stops[next_stop] {
                    continue
                }
                vis_stops[next_stop] = true

                q = append(q, [2]int{next_stop, dist + 1})
            }
        }
    }

    return -1
}