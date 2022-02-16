import pandas as pd

from instabot import Bot
from src.settings import INSTA_USER, INSTA_PASS

bot = Bot()
bot.login(
    username=INSTA_USER,
    password=INSTA_PASS,
)


to_follow = bot.get_user_followers("milkhoneysoul")
to_follow_df = pd.DataFrame(to_follow, columns=['followers'])

no_follow = bot.get_user_following('special_cuts')
no_follow_df = pd.DataFrame(no_follow, columns=['following'])

# TODO: only follow those users who aren't already being followed
# to_follow_df[]
bot.follow('username')



# TODO: setup clean up of non followers
bot.unfollow_non_followers()