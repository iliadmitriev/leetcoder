
var (
	digits = [20]string{
		"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
		"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
	}

	tens = [10]string{
		"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
	}
)

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	return numberToStringHelper(num)
}

func numberToStringHelper(num int) string {
	v := strings.Builder{}

	if num < 20 {
		v.WriteString(digits[num])
	} else if num < 100 {
		v.WriteString(tens[num/10])
		v.WriteString(" ")
		v.WriteString(numberToStringHelper(num % 10))
	} else if num < 1000 {
		v.WriteString(digits[num/100])
		v.WriteString(" Hundred ")
		v.WriteString(numberToStringHelper(num % 100))
	} else if num < 1000000 {
		v.WriteString(numberToStringHelper(num / 1000))
		v.WriteString(" Thousand ")
		v.WriteString(numberToStringHelper(num % 1000))
	} else if num < 1000000000 {
		v.WriteString(numberToStringHelper(num / 1000000))
		v.WriteString(" Million ")
		v.WriteString(numberToStringHelper(num % 1000000))
	} else {
		v.WriteString(numberToStringHelper(num / 1000000000))
		v.WriteString(" Billion ")
		v.WriteString(numberToStringHelper(num % 1000000000))
	}

	s := v.String()
	if len(s) > 0 && s[len(s)-1] == ' ' {
		s = s[:len(s)-1]
	}

	return s
}
