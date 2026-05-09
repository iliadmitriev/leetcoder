class Solution:
    def get_most_cover(self, clips: List[List[int]], start: int) -> int:
        """
        Get biggest length from clips which starts from start or earlier (covers)
        and gives biggest length.
        Returns: delta time
        """
        most = -1
        for clip in clips:
            diff = clip[1] - start
            if clip[0] <= start and most < diff:
                most = diff

        return most

    def videoStitching(self, clips: List[List[int]], time_to_cover: int) -> int:
        # current length covered
        cur = 0
        # current length covered starting from current timestamp
        most = self.get_most_cover(clips, cur)
        # number of resulting cuts
        result = 0

        # iterate while current time is still les then time to cover (didn't reached the end)
        # and there is a clip which start from current or earlier and gives positive length
        while cur < time_to_cover and most > 0:
            # add another cut
            result += 1
            # add covered length to cur covered length
            cur += most
            # get another max length possible to cover from clips 
            most = self.get_most_cover(clips, cur)

        return result if cur >= time_to_cover else -1