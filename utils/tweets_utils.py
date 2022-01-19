import re
import string
from tkinter import E
import emoji


def clean_tweet(text):

    # replace retweet username
    # RT @user_name: ...tweet text...
    # some @user_id has 3 characters such as @CNN
    # some mentioned accounts are hashed so I included + and =
    rt_re = r"^RT\s\@[a-zA-Z0-9_+=]{3,}:\s"
    text = re.sub(rt_re, "", text)

    # replace user name
    user_re = r"\@[a-zA-Z0-9_+=]{3,}"
    text = re.sub(user_re, "", text)

    # replace url
    url_re = r"https?\S+"
    text = re.sub(url_re, "", text)

    # replace hashtag sign
    hashtag_re = "#"
    text = re.sub(hashtag_re, "", text)

    # replace escape char
    escape_re = "\n"
    text = re.sub(escape_re, "", text)

    # replace punctuation
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string

    # clean starting space
    space_re = "^\s"
    text = re.sub(space_re, "", text)

    return text


def get_emojis(text):
    # https://stackoverflow.com/questions/43146528/how-to-extract-all-the-emojis-from-text
    demojised_text = emoji.demojize(text)
    emoji_re = r"(:[!_\-\w]+:)"
    extracted_emojis = re.findall(emoji_re, demojised_text)
    return [emoji.emojize(i) for i in extracted_emojis]


# user id in tweet_text column can be hashed
def get_mentioned_accounts(text):
    pattern = "\@[a-zA-Z0-9_+=]{3,}"
    users = re.findall(pattern, text)
    return users


def get_rt_account(text):
    # the retweet raw text starts with RT
    pattern = "^RT\s(\@[a-zA-Z0-9_+=]{3,})"
    user = re.findall(pattern, text)
    return user