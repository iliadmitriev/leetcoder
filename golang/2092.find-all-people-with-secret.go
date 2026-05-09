func dfs(start int, adj map[int][]int, vis map[int]bool, resMap map[int]bool) {
    if vis[start] {
        return
    }

    vis[start] = true
    resMap[start] = true

    for _, child := range adj[start] {
        dfs(child, adj, vis, resMap)
    }
}

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {

    secretsMap := map[int]bool{0: true, firstPerson: true}

    timeMap := make(map[int]map[int][]int)

    for _, meeting := range meetings {
        src, dst, time := meeting[0], meeting[1], meeting[2]
        if timeMap[time] == nil {
            timeMap[time] = make(map[int][]int)
        }

        timeMap[time][src] = append(timeMap[time][src], dst)
        timeMap[time][dst] = append(timeMap[time][dst], src)
    }

    timeList := make([]int, 0, len(timeMap))
    for time, _ := range timeMap {
        timeList = append(timeList, time)
    }

    sort.Ints(timeList)

    for _, time := range timeList {
        visited := make(map[int]bool)

        for src, _ := range timeMap[time] {
            if secretsMap[src] {
                dfs(src, timeMap[time], visited, secretsMap)
            }
        }
    }

    secrets := make([]int, 0, len(secretsMap))
    for src, _ := range secretsMap {
        secrets = append(secrets, src)
    }

    return secrets
}