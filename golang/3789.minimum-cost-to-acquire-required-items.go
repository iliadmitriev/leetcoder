func minimumCost(cost1 int, cost2 int, costBoth int, need1 int, need2 int) int64 {
    totalCost := 0
    
    if cost1 + cost2 <= costBoth {
        totalCost += cost1 * need1 + cost2 * need2
    } else {
        needBoth := min(need1, need2)
        totalCost += needBoth * costBoth;
        
        need1 -= needBoth
        need2 -= needBoth
        
        totalCost += need1 * min(costBoth, cost1)
        totalCost += need2 * min(costBoth, cost2)
    }
    
    return int64(totalCost)
}