type ParkingSystem struct {
    free map[int]int
}


func Constructor(big int, medium int, small int) ParkingSystem {
    free := map[int]int{1: big, 2: medium, 3: small}
    return ParkingSystem{ free }
}


func (this *ParkingSystem) AddCar(carType int) bool {
    if this.free[carType] > 0 {
        this.free[carType]--
        return true
    }
    return false
}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */