func swap(a *int, b *int) {
    *a, *b = *b, *a;
}

func gen(nums *[]int, curr int, res *[][]int) {
    if len(*nums) == curr {
        temp := make([]int, len(*nums))
        copy(temp, *nums)
        *res = append(*res, temp)
        return;
    }

    for i := curr; i < len(*nums); i++ {
        swap(&(*nums)[i], &(*nums)[curr])
        gen(nums, curr + 1, res)
        swap(&(*nums)[i], &(*nums)[curr])
    }
}

func permute(nums []int) [][]int {
    res := [][]int{}
    gen(&nums, 0, &res)
    return res
}