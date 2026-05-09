func daysBetweenDates(date1 string, date2 string) int {
	d1, _ := time.Parse("2006-01-02", date1)
	d2, _ := time.Parse("2006-01-02", date2)

	if d1.After(d2) {
		d1, d2 = d2, d1
	}

	return int(d2.Sub(d1).Hours() / 24)
}
