import (
    "container/heap"
)

type FoodInfo struct {
    Name string
    Cuisine string
    Rating int
}

type FoodRatings struct {
    Cuisine map[string]*MaxHeap
    Food map[string]FoodInfo
}

// O(n * log(n))
func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
    cuisineToInfoHeap := make(map[string]*MaxHeap)
    foodToInfo := make(map[string]FoodInfo)

    for i := 0; i < len(foods); i++ {
        foodInfo := FoodInfo{foods[i], cuisines[i], ratings[i]}

        foodToInfo[foods[i]] = foodInfo

        // if there is no cuisine in the map
        // then init with new empty MaxHeap
        if _, ok := cuisineToInfoHeap[cuisines[i]]; !ok {
            cuisineToInfoHeap[cuisines[i]] = &MaxHeap{}
        }

        heap.Push(cuisineToInfoHeap[cuisines[i]], foodInfo)
    }

    return FoodRatings{
        cuisineToInfoHeap,
        foodToInfo,
    }
}

// O(log(n))
func (this *FoodRatings) ChangeRating(food string, newRating int)  {
    if toUpdate, ok := this.Food[food]; ok {
        toUpdate.Rating = newRating
        this.Food[food] = toUpdate
    }
    cuisine := this.Food[food].Cuisine

    heap.Push(this.Cuisine[cuisine], FoodInfo{food, cuisine, newRating})

}


func (this *FoodRatings) HighestRated(cuisine string) string {
    highRatedFood := this.Cuisine[cuisine].Top()
    // for all if top value rating is not equal to current rating
    // entry is old, then throw it away
    for highRatedFood.Rating != this.Food[highRatedFood.Name].Rating {
        heap.Pop(this.Cuisine[cuisine])
        highRatedFood = this.Cuisine[cuisine].Top()
    }

    return highRatedFood.Name
}


/**
* MaxHeap realization
*/

type MaxHeap []FoodInfo

func (h MaxHeap) Len() int {return len(h)}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h MaxHeap) Less(i, j int) bool {
    if h[i].Rating == h[j].Rating {
        return h[i].Name < h[j].Name
    }
    return h[i].Rating > h[j].Rating
}

func (h *MaxHeap) Push(x interface{}) {
    *h = append(*h, x.(FoodInfo))
}

func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[:n - 1]
    return x
}

func (h *MaxHeap) Top() FoodInfo {
    return (*h)[0]
}
