from instabot import Bot

# Login
bot = Bot()
bot.login(username = "yourUsername", password = "yourPaswwrod")

# Follow
Bot.follow("username_you_want_to_follow")

# Follow more than one person
list_of_user = ["username_you_want_to_follow", "another_username", ....]
Bot.follow_users(list_of_user)

# Unfollow one person
Bot.unfollow("username_you_want_to_unfollow")

# Unfollow more than one person
unfollowUsers = ["username_you_want_to_unfollow", "another_username", ....]
Bot.follow_users(unfollowUsers)

#Count number of followers
follower = Bot.get_user_followers("username")
print("Total number of followers: ")
print(len(follower))

# Send messages
message = "I don't dislike you"
Bot.send_message(message, "username")

#