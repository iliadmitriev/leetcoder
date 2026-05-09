func getDirections(root *TreeNode, startValue int, destValue int) string {
	startPath := []byte{}
	_ = nodePath(root, startValue, &startPath)
	destPath := []byte{}
	_ = nodePath(root, destValue, &destPath)

	i, j := len(startPath)-1, len(destPath)-1
	for i >= 0 && j >= 0 && startPath[i] == destPath[j] {
		i--
		j--
	}
	startPath = startPath[:i+1]
	destPath = destPath[:j+1]

	for i := 0; i < len(startPath); i++ {
		startPath[i] = 'U'
	}

	return string(startPath) + string(reversePath(destPath))
}

func reversePath(path []byte) []byte {
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}

func nodePath(root *TreeNode, value int, path *[]byte) bool {
	if root == nil {
		return false
	}

	if root.Val == value {
		return true
	}

	if ok := nodePath(root.Left, value, path); ok {
		*path = append(*path, 'L')
		return true
	}

	if ok := nodePath(root.Right, value, path); ok {
		*path = append(*path, 'R')
		return true
	}

	return false
}
