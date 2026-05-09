func reformatDate(date string) string {
	j := 0
	for j < len(date) && date[j] >= '0' && date[j] <= '9' {
		j++
	}

	num := date[j : j+2]
	format := fmt.Sprintf("2%s Jan 2006", num)
	t, _ := time.Parse(format, date)
	return t.Format("2006-01-02")
}
