import (
	"strconv"
	"strings"
)

const (
	OPERATOR = "+"
)

type Spreadsheet struct {
	sheet map[string]int
}

func Constructor(rows int) Spreadsheet {
	return Spreadsheet{
		sheet: make(map[string]int),
	}
}

func (this *Spreadsheet) SetCell(cell string, value int) {
	this.sheet[cell] = value
}

func (this *Spreadsheet) ResetCell(cell string) {
	delete(this.sheet, cell)
}

func (this *Spreadsheet) formula(formula string) (string, string) {
	res := strings.Split(formula[1:], OPERATOR)
	return res[0], res[1]
}

func (this *Spreadsheet) getTarget(s string) int {
	switch {
	case '0' <= s[0] && s[0] <= '9':
		v, _ := strconv.Atoi(s)
		return v
	case 'A' <= s[0] && s[0] <= 'Z':
		return this.sheet[s]
	default:
		return 0
	}
}

func (this *Spreadsheet) GetValue(formula string) int {
	op1, op2 := this.formula(formula)
	v1, v2 := this.getTarget(op1), this.getTarget(op2)

	return v1 + v2
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * obj := Constructor(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * param_3 := obj.GetValue(formula);
 */