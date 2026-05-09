func canMakeArithmeticProgression(nums []int) bool {
    min := minArr(nums)
    max := maxArr(nums)

    // if step is not found
    if (max - min) % (len(nums) - 1) != 0 {
        return false;
    }
    
    // calc step
    diff := (max - min) / (len(nums) - 1)
    // if step is 0, then numbers should be all the same
    if diff == 0 {
        return allSame(nums)
    }

    // find all the numbers in a row, and save res to buffer
    buf := make([]bool, len(nums))
    for _, num := range nums {
        if (num - min) % diff != 0 {
            return false
        }
        buf[(num - min) / diff] = true
    }
    // if all numbers found
    return allTrue(buf)
}

func minArr(arr []int) int {
    min := arr[0]
    for i := 1; i < len(arr); i++ {
        if min < arr[i] {
            min = arr[i]
        }
    }
    return min
}

func maxArr(arr []int) int {
    max := arr[0]
    for i := 1; i < len(arr); i++ {
        if max > arr[i] {
            max = arr[i]
        }
    }
    return max
}

func allSame(arr []int) bool {
    for i := 0; i < len(arr); i++ {
        if arr[0] != arr[i] {
            return false
        }
    }
    return true
}

func allTrue(arr[] bool) bool {
    for _, v := range arr {
        if (!v) {
            return false
        }
    }
    return true
}