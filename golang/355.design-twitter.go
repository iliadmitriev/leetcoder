package main

import "container/heap"

type Tweet struct {
	TweetID   int
	TimeStamp int
	Next      *Tweet
}

type MaxHeap []*Tweet

func (h MaxHeap) Len() int            { return len(h) }
func (h MaxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h MaxHeap) Less(i, j int) bool  { return h[i].TimeStamp > h[j].TimeStamp }
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(*Tweet)) }
func (h *MaxHeap) Pop() interface{} {
	n := len(*h) - 1
	x := (*h)[n]
	*h = (*h)[:n]
	return x
}

type Twitter struct {
	Followee  map[int]map[int]struct{}
	Tweets    map[int]*Tweet
	TimeStamp int
}

func Constructor() Twitter {
	followee := make(map[int]map[int]struct{})
	tweets := make(map[int]*Tweet)
	return Twitter{followee, tweets, 0}
}

func (this *Twitter) PostTweet(userId int, tweetId int) {
	this.TimeStamp++
	this.Tweets[userId] = &Tweet{tweetId, this.TimeStamp, this.Tweets[userId]}
}

func (this *Twitter) GetNewsFeed(userId int) []int {
	feed := make([]int, 0, 10)

	maxHeap := &MaxHeap{}
	heap.Init(maxHeap)

	if this.Tweets[userId] != nil {
		heap.Push(maxHeap, this.Tweets[userId])
	}

	for followee := range this.Followee[userId] {
		if this.Tweets[followee] != nil {
			heap.Push(maxHeap, this.Tweets[followee])
		}
	}

	for len(feed) < 10 && maxHeap.Len() > 0 {
		tweet := heap.Pop(maxHeap).(*Tweet)
		feed = append(feed, tweet.TweetID)

		if tweet.Next != nil {
			heap.Push(maxHeap, tweet.Next)
		}
	}

	return feed
}

func (this *Twitter) Follow(followerId int, followeeId int) {
	if this.Followee[followerId] == nil {
		this.Followee[followerId] = map[int]struct{}{}
	}

	this.Followee[followerId][followeeId] = struct{}{}
}

func (this *Twitter) Unfollow(followerId int, followeeId int) {
	delete(this.Followee[followerId], followeeId)
}

/**
 * Your Twitter object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PostTweet(userId,tweetId);
 * param_2 := obj.GetNewsFeed(userId);
 * obj.Follow(followerId,followeeId);
 * obj.Unfollow(followerId,followeeId);
 */