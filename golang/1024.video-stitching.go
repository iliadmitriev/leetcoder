// Returns: max time length can be covered starting from startTimestamp (or earlier)
// -1 if can't be covered
func getMaxLength(clips [][]int, startTimestamp int) int {
    maxLength := -1
    for _, clip := range clips {
        curLength := clip[1] - startTimestamp
        if clip[0] <= startTimestamp && maxLength < curLength {
            maxLength = curLength
        }
    }
    return maxLength
}

func videoStitching(clips [][]int, timeToCover int) int {
    // start from 0 timestamp
    currTime := 0
    // get how much max length be covered from current timestamp with a stitch
    currStitchLength := getMaxLength(clips, currTime)
    // result: number of video stitches needed
    stitchesCount := 0

    // repeat while current timestamp is less than time needed to cover
    // and there is a stitch that can add more time to full length (length > 0)
    for  ; currTime < timeToCover && currStitchLength > 0;  {
        // add stitch to full movie
        stitchesCount++
        currTime += currStitchLength
        // get next possible max stitch
        currStitchLength = getMaxLength(clips, currTime)   
    }
    // if full movie is covered by up to current time then return number of stitches 
    if currTime >= timeToCover {
        return stitchesCount
    }
    return -1
}