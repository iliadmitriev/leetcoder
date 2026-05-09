func minimumReplacement(nums []int) (replacements int64) {
    n := len(nums)

    // iterate all nums in reverse order starting from last but one
    // (last is always sorted)
    for i := n - 2; i >= 0; i-- {
        // if nothing to do skip (already sorted in non descending order)
        if nums[i] <= nums[i + 1] {
            continue
        }

        // count number of newly elements created after the replacement operation
        new_count := (nums[i] + nums[i + 1] - 1) / nums[i + 1]

        // add number of repalcements to the answer (count - 1)
        replacements += int64(new_count - 1)

        // find leftmost element after the replacement
        nums[i] /= new_count

    }

    return
}