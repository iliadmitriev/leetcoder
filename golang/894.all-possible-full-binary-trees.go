func allPossibleFBT(n int) []*TreeNode {
    
    dp := make(map[int][]*TreeNode, 0)

    var allPossibleFBTFor func(n int) []*TreeNode
    allPossibleFBTFor = func(n int) []*TreeNode {
        if n == 0 || n % 2 == 0 {
            return []*TreeNode{}
        } else if n == 1 {
            return []*TreeNode{&TreeNode{0, nil, nil}}
        } else if n == 3 {
            return []*TreeNode{&TreeNode{0, &TreeNode{}, &TreeNode{}}}
        }

        if _, prs := dp[n]; prs {
            return dp[n]
        }

        fbts := make([]*TreeNode, 0)
        // we only have n nodes since root of this subtree used one
        for i := 0; i < n; i += 1 {
            for _, leftSubtree := range allPossibleFBTFor(i) {
                for _, rightSubtree := range allPossibleFBTFor(n - 1 - i) {
                    root := TreeNode{}
                    root.Left = leftSubtree
                    root.Right = rightSubtree
                    fbts = append(fbts, &root)
                }
            }    
        }
        
        dp[n] = make([]*TreeNode, len(fbts))
        copy(dp[n], fbts)
        return dp[n]
    }

    return allPossibleFBTFor(n)
}