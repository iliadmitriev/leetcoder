class Solution {
private:
    // Returns: max time length can be covered starting from startTimestamp (or earlier)
    // -1 if can't be covered
    int getMostLength(vector<vector<int>>& clips, int startTimestamp) {
        int mostCoveredLength = -1;
        for (const auto& clip : clips) {
            int coveredLength = clip[1] - startTimestamp;
            if (clip[0] <= startTimestamp && mostCoveredLength < coveredLength) {
                mostCoveredLength = coveredLength;
            }
        }
        return mostCoveredLength;
    }
public:
    int videoStitching(vector<vector<int>>& clips, int timeToCover) {
        // start from 0 timestamp
        int currTime = 0;
        // get how much time at maximum can be covered from current timestamp
        int mostCovered = getMostLength(clips, currTime);
        // result: number of video stitches needed
        int stitchCounter = 0;

        // repeat while current timestamp is less than time needed to cover
        // and there is a stitch that can add more time to full length (length > 0)
        while (currTime < timeToCover && mostCovered > 0) {
            stitchCounter++;
            // add stitch to full movie
            currTime += mostCovered;
            // get next possible max stitch
            mostCovered = getMostLength(clips, currTime);
        }

        // if full movie covered then return number of stitches 
        if (currTime >= timeToCover)
            return stitchCounter;
        return -1;
    }
};