func minimumPairRemoval(nums []int) int {
    
    isAscending := false
    removes := 0

    for !isAscending && len(nums) > 1 {
      minIdx := 1
      minSum := nums[0] + nums[1]
      isAscending = true

      for i := 1; i < len(nums); i++ {
        if nums[i-1] > nums[i] {
          isAscending = false
        }

        sum := nums[i - 1] + nums[i]
        if sum < minSum {
          minIdx = i
          minSum = sum
        }
      }

      if isAscending {
        break
      }

      removes++
      tmp := nums[minIdx+1:]
      nums = append(nums[:minIdx-1], minSum)
      nums = append(nums, tmp...)
    }

    return removes
}