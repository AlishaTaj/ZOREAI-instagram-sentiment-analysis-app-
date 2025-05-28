import instaloader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
from instaloader import Profile

# 🔐 Login credentials — use a test account
IG_USERNAME = "insta.bot.test"
IG_PASSWORD = "botpassword123"

def login_loader():
    loader = instaloader.Instaloader()
    try:
        loader.login(IG_USERNAME, IG_PASSWORD)
        loader.context.request_timeout = 10
        loader.context.raise_all_errors = False
        loader.context.max_connection_attempts = 1
    except Exception as e:
        print("Login failed:", e)
    return loader

def getPublicProfileCaptions(profile_id):
    loader = login_loader()
    try:
        profile = Profile.from_username(loader.context, profile_id)
    except Exception as e:
        return "Instagram blocked this request. Please try again later.", "Empty", "Empty", []

    profile_pic = profile.get_profile_pic_url()
    full_name = profile.full_name
    posts = profile.get_posts()
    captions = []
    posts_data = []

    for post in posts:
        if post.caption:
            captions.append(post.caption)
            posts_data.append({
                'url': post.url,
                'likes': post.likes,
                'date': str(post.date),
            })

    loader.close()

    if len(captions) < 1:
        return "No captions found! Are you sure this profile is public and has posted?", "Empty", "Empty", []

    return captions, profile_pic, full_name, posts_data


def getPrivateProfileCaptions(profile_id, login, password):
    loader = instaloader.Instaloader()
    try:
        loader.login(login, password)
    except:
        return "Failed to login!", "Empty", "Empty", []

    try:
        profile = Profile.from_username(loader.context, profile_id)
    except:
        return "Could not fetch profile. Possibly incorrect username.", "Empty", "Empty", []

    posts = profile.get_posts()
    profile_pic = profile.get_profile_pic_url()
    full_name = profile.full_name
    captions = []
    posts_data = []

    for post in posts:
        if post.caption:
            captions.append(post.caption)
            posts_data.append({
                'url': post.url,
                'likes': post.likes,
                'date': str(post.date),
            })

    loader.close()

    if len(captions) < 1:
        return "No captions found! Are you sure this profile has posted?", "Empty", "Empty", []

    return captions, profile_pic, full_name, posts_data


def getSentiments(captions_or_comments):
    if len(captions_or_comments) > 0 and isinstance(captions_or_comments, list):
        analyser = SentimentIntensityAnalyzer()
        neutral = []
        positive = []
        negative = []
        compound = []

        for text in captions_or_comments:
            scores = analyser.polarity_scores(text)
            neutral.append(scores['neu'])
            positive.append(scores['pos'])
            negative.append(scores['neg'])
            compound.append(scores['compound'])

        return {
            'Neutral': round(np.mean(neutral) * 100, 2),
            'Positive': round(np.mean(positive) * 100, 2),
            'Negative': round(np.mean(negative) * 100, 2),
            'Overall': round(np.mean(compound) * 100, 2)
        }
    return {"error": "No valid input for sentiment analysis"}
