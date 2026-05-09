package main

type Point [2]int

var dirs = []Point{{1, 0}, {0, 1}}

func findFarmlandBound(land [][]int, start Point, visited [][]bool) Point {
	maxX, maxY := len(land[0]), len(land)
	q := []Point{start}
	visited[start[0]][start[1]] = true
	var p Point

	for len(q) > 0 {
		p = q[0]
		q = q[1:]

		for _, d := range dirs {
			y, x := p[0]+d[0], p[1]+d[1]
			if x < 0 || x >= maxX || y < 0 || y >= maxY || visited[y][x] || land[y][x] == 0 {
				continue
			}

			visited[y][x] = true
			q = append(q, Point{y, x})
		}
	}

	return p
}

func findFarmland(land [][]int) [][]int {
	maxX, maxY := len(land[0]), len(land)
	visited := make([][]bool, maxY)
	for i := range visited {
		visited[i] = make([]bool, maxX)
	}

	res := [][]int{}

	for y := 0; y < maxY; y++ {
		for x := 0; x < maxX; x++ {
			if land[y][x] == 1 && !visited[y][x] {
				bound := findFarmlandBound(land, Point{y, x}, visited)
				res = append(res, []int{y, x, bound[0], bound[1]})
			}
		}
	}

	return res
}
