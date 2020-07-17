# 355. 设计推特
# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。
# 你的设计需要支持以下的几个功能：
    # postTweet(userId, tweetId): 创建一条新的推文
    # getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
    # follow(followerId, followeeId): 关注一个用户
    # unfollow(followerId, followeeId): 取消关注一个用户


class Twitter:
    def __init__(self):
        self.time = 0
        self.twitters = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.twitters.__contains__(userId):
            self.twitters[userId].insert(0, [self.time, tweetId])
            self.time += 1
        else:
            self.twitters[userId] = [[self.time, tweetId]]
            self.time += 1

    def getNewsFeed(self, userId: int):
        twitters = []
        userIds = [userId]
        if self.following.__contains__(userId):
            userIds = [userId, *self.following[userId]]
        for uid in userIds:
            if self.twitters.__contains__(uid):
                twitters.extend(self.twitters[uid][:10])
        twitters.sort(reverse=True)
        res = [item[1] for item in twitters[:10]]
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if self.following.__contains__(followerId):
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if self.following.__contains__(followerId):
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print('1 : ', twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print('2 : ', twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print('3 : ', twitter.getNewsFeed(1))
    print()

    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    print('1 : ', twitter.getNewsFeed(1))
    print()

    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.follow(1, 1)
    print('1 : ', twitter.getNewsFeed(1))
    print()