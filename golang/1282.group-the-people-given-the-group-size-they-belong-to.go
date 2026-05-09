func groupThePeople(groupSizes []int) [][]int {
    groups := make([][]int, 0, len(groupSizes))
    maxGroupSize := 0
    for person, groupSize := range groupSizes {
        groups = append(groups, []int{groupSize, person})
        if maxGroupSize < groupSize {
            maxGroupSize = groupSize
        }
    }

    sort.Slice(groups, func(i, j int) bool {
        return groups[i][0] < groups[j][0] ||
             (groups[i][0] == groups[j][0] &&
              groups[i][1] < groups[j][1])
    })

    assigned := make([][]int, 0)
    currGroup := make([]int, 0, maxGroupSize)

    for _, person := range groups {
        currGroup = append(currGroup, person[1])

        if len(currGroup) == person[0] {
            // add copy to result
            groupCopy := make([]int, len(currGroup))
            copy(groupCopy, currGroup)
            assigned = append(assigned, groupCopy)

            // reset slice
            currGroup = currGroup[:0]
        }
    }

    return assigned
}