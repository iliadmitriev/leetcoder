import (
	"slices"
)

type robot struct {
	idx, health, pos int
	dir              byte
}

type stack[T any] []T

func NewStack[T any](cap int) *stack[T] {
	st := make(stack[T], 0, cap)
	return &st
}

func (s *stack[T]) push(x T) {
	*s = append(*s, x)
}

func (s *stack[T]) pop() T {
	x := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]

	return x
}

func (s *stack[T]) top() T {
	return (*s)[len(*s)-1]
}

func (s *stack[T]) empty() bool {
	return len(*s) == 0
}

func (s *stack[T]) sort(f func(a, b T)int) {
	slices.SortFunc(*s, f)
}

func mapper[T, U any](s *stack[T], f func(a T) U) []U {
  res := make([]U, 0, len(*s))
  for _, v := range *s {
    res = append(res, f(v))
  }

  return res
}

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {

	n := len(positions)
	if n != len(healths) || n != len(directions) {
		return nil
	}

	robots := make([]robot, 0, n)
	for i := range n {
		robots = append(robots, robot{i, healths[i], positions[i], directions[i]})
	}

	slices.SortFunc(robots, func(a, b robot) int {
		return a.pos - b.pos
	})

	st := NewStack[robot](n)

	for _, rob := range robots {
		// if there is a robot in stack moves right also current robot is alive and moves left
		// definatelly there is a collision
		for !st.empty() && st.top().dir == 'R' && rob.dir == 'L' && rob.health > 0 {
			top := st.pop()

			if top.health > rob.health {
				rob.health = 0 // currend dead
				top.health--   // from stack is damaged
				st.push(top)   // but still alive
			} else if top.health < rob.health {
				rob.health-- // current is damaged
			} else { // eq => both dead
				rob.health = 0
			}
		}

		if rob.health > 0 {
			st.push(rob)
		}

	}

  st.sort(func(a, b robot) int {
		return a.idx - b.idx
	})

	return mapper(st, func(a robot) int {
    return a.health
  })
}