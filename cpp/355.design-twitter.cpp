#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Tweet {
public:
  int id;
  int timestamp;
  Tweet *next;

  Tweet(int id, int timestamp, Tweet *next)
      : id(id), timestamp(timestamp), next(next) {}

  int getId() const { return id; }

  bool operator<(const Tweet &other) const {
    return timestamp < other.timestamp;
  }
};

class Twitter {
private:
  unordered_map<int, Tweet *> tweets; // userId -> latest tweet
  unordered_map<int, unordered_set<int>>
      userFollows; // userId -> set of followee Ids
  int timer;

public:
  Twitter() : timer(0) {}

  void postTweet(int userId, int tweetId) {
    tweets[userId] = new Tweet(tweetId, timer--, tweets[userId]);
  }

  vector<int> getNewsFeed(int userId) {
    priority_queue<Tweet *> minHeap;
    if (tweets[userId] != nullptr) {
      minHeap.push(tweets[userId]);
    }

    for (int followeeId : userFollows[userId]) {
      if (tweets[followeeId] != nullptr) {
        minHeap.push(tweets[followeeId]);
      }
    }

    vector<int> newsFeed;

    while (minHeap.size() && newsFeed.size() < 10) {
      auto tweet = minHeap.top();
      minHeap.pop();

      newsFeed.push_back(tweet->getId());

      if (tweet->next) {
        minHeap.push(tweet->next);
      }
    }

    return newsFeed;
  }

  void follow(int followerId, int followeeId) {
    userFollows[followerId].insert(followeeId);
  }

  void unfollow(int followerId, int followeeId) {
    userFollows[followerId].erase(followeeId);
  }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */