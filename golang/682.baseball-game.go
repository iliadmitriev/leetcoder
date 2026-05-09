func calPoints(operations []string) int {
	line := make([]int, 0, len(operations))

	for _, op := range operations {
		switch op {
		case "C":
			line = line[:len(line)-1]
		case "D":
			line = append(line, 2*line[len(line)-1])
		case "+":
			line = append(line, line[len(line)-1]+line[len(line)-2])
		default:
			v, _ := strconv.Atoi(op)
			line = append(line, v)
		}
	}

	return arrSum(line)
}

func arrSum(arr []int) int {
	s := 0
	for _, v := range arr {
		s += v
	}
	return s
}
