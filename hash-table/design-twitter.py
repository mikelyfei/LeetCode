import heapq

class Tweet:
    def __init__(self, tweetId, time, next_tweet=None):
        self.tweetId = tweetId
        self.time = time
        self.next = next_tweet

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)   # follower -> {followees}
        self.tweetMap = {}                  # userId -> latest Tweet node

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        new_tweet = Tweet(tweetId, self.time, self.tweetMap.get(userId))
        self.tweetMap[userId] = new_tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = set(self.followMap[userId])
        users.add(userId)

        for user in users:
            tweet = self.tweetMap.get(user)
            while tweet:
                heapq.heappush(heap, [-tweet.time, tweet.tweetId])
                tweet = tweet.next
        tweets = []
        for i in range(10):
            if heap:
                minus_tweet_time, tweetId = heapq.heappop(heap)
                tweets.append(tweetId)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)