class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        min_heap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][idx]
                min_heap.append((count, tweetId, followeeId, idx - 1))
        heapq.heapify(min_heap)
        while min_heap and len(feed) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(min_heap)
            feed.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(min_heap, (count, tweetId, followeeId, idx - 1))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
