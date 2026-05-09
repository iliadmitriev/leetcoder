import heapq
from collections import defaultdict
from typing import List, Optional, Self


class Tweet:
    __slots__ = ("tweetId", "timestamp", "next")

    def __init__(self, tweetId: int, timestamp: int, next: Optional[Self] = None):
        self.tweetId = tweetId
        self.timestamp = timestamp
        self.next = next

    def __lt__(self, other: Self) -> bool:
        return self.timestamp < other.timestamp

    def __gt__(self, other: Self) -> bool:
        return self.timestamp > other.timestamp

    def __repr__(self) -> str:
        return f"Tweet({self.tweetId}, {self.timestamp})"


class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(set)
        self.tweets = defaultdict(lambda: None)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId] = Tweet(tweetId, self.time, self.tweets[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets: list[Tweet] = []
        for followee in self.users[userId]:
            tweet = self.tweets[followee]
            if tweet is not None:
                tweets.append(tweet)

        my_tweets = self.tweets[userId]
        if my_tweets:
            tweets.append(my_tweets)

        heapq.heapify(tweets)

        res: list[int] = []
        while len(res) < 10 and tweets:
            tweet = heapq.heappop(tweets)
            res.append(tweet.tweetId)

            if tweet.next:
                heapq.heappush(tweets, tweet.next)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)