func findSpecialInteger(arr []int) int {
    n := len(arr)

    res := arr[0]
    count := 1

    for i := 1; i < n; i++ {
        
        if arr[i - 1] == arr[i] {
            count++
        } else {
            count = 1
        }

        if count > n / 4 {
            res = arr[i]
            break
        }
    }
        
    return res
}