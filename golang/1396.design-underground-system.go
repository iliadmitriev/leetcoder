type UndergroundSystem struct {
    time map[string]int
    count map[string]int
    checkInTime map[int]int
    checkInStation map[int]string
}


func Constructor() UndergroundSystem {
    return UndergroundSystem{
        make(map[string]int),
        make(map[string]int),
        make(map[int]int),
        make(map[int]string),
    }
}


func (this *UndergroundSystem) CheckIn(id int, stationName string, t int)  {
    this.checkInTime[id] = t
    this.checkInStation[id] = stationName
}


func (this *UndergroundSystem) CheckOut(id int, stationName string, t int)  {
    startStation := this.checkInStation[id]
    startTime := this.checkInTime[id]
    key := startStation + "*" + stationName
    this.time[key] += t - startTime
    this.count[key]++
}


func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
    key := startStation + "*" + endStation
    totalTime := float64(this.time[key])
    totalCout := float64(this.count[key])
    if totalCout > 0 {
        return totalTime / totalCout
    }
    return 0.0
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */