type Robot struct {
	width, height int  // width and height
	steps         int  // number of steps done
	per           int  // area perimeter
	moved         bool // is robot ever moved
}

/* 
⬅️⬅️⬅️⬅️⬅️⬆️
⬇️        ⬆️
⬇️        ⬆️
⬇️        ⬆️
⬇️➡️➡️➡️➡️➡️
*/

var dirs [4]string = [4]string{"East", "North", "West", "South"}

func Constructor(width int, height int) Robot {
	per := (height - 1 + width - 1) * 2 // perimeter

	return Robot{
		width:  width,
		height: height,
		per:    per,
	}
}

func (this *Robot) Step(num int) {
	this.moved = true
	this.steps = (this.steps + num) % this.per
}

func (this *Robot) GetPos() []int {
	switch {
	case this.steps <= this.width-1:
		return []int{this.steps, 0}
	case this.steps <= this.width+this.height-2:
		return []int{this.width - 1, this.steps - this.width + 1}
	case this.steps <= this.width*2+this.height-3:
		return []int{this.width - (this.steps - this.width - this.height + 3), this.height - 1}
	default:
		return []int{0, this.per - this.steps}
	}
}

func (this *Robot) GetDir() string {
	if !this.moved {
		return dirs[0]
	}

	switch {
	case this.steps == 0:
		return dirs[3]
	case this.steps <= this.width-1:
		return dirs[0]
	case this.steps <= this.width+this.height-2:
		return dirs[1]
	case this.steps <= this.width*2+this.height-3:
		return dirs[2]
	default:
		return dirs[3]
	}
}

/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Step(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
 */