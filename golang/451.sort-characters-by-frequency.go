import (
    "fmt"
)

type Item struct {
    b byte
    i int
}

func frequencySort(s string) string {
    cache := make([]int, 250)
    for i := range s {
        cache[s[i] - 'a']++
    }

    cache2 := make([]Item, 0, 200)
    for i := range cache {
        if cache[i] > 0 {
            cache2 = append(cache2, Item{byte('a' + i), cache[i]})
        }
    }

    sort.Slice(cache2, func (i, j int) bool {
        if cache2[i].i == cache2[j].i {
            return cache2[i].b < cache2[j].b
        }
        return cache2[i].i > cache2[j].i
    })

    fmt.Println(cache2)
    res := make([]byte, len(s))
    i := 0

    for j := range cache2 {
        for k := 0; k < cache2[j].i; k++ {
            res[i] = cache2[j].b
            i++
        }
    }

    return string(res)
}