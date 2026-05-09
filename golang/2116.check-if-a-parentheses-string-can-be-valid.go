func canBeValid(s string, locked string) bool {
	stackFree := make([]int, 0, len(s))
	stackLocked := make([]int, 0, len(s))

	for i := 0; i < len(s); i++ {
		if locked[i] == '0' {
			stackFree = append(stackFree, i)
		} else {
			if s[i] == '(' {
				stackLocked = append(stackLocked, i)
			} else {
				if len(stackLocked) > 0 {
					stackLocked = stackLocked[:len(stackLocked)-1]
				} else if len(stackFree) > 0 {
					stackFree = stackFree[:len(stackFree)-1]
				} else {
					return false
				}
			}
		}
	}

	for len(stackLocked) > 0 && len(stackFree) > 0 {
		topLock := stackLocked[len(stackLocked)-1]
		topFree := stackFree[len(stackFree)-1]

		if topLock > topFree {
			return false
		}

		stackLocked = stackLocked[:len(stackLocked)-1]
		stackFree = stackFree[:len(stackFree)-1]
	}

	return len(stackLocked) == 0 && len(stackFree)%2 == 0
}
