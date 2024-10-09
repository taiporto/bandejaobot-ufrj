from atproto import models
from bluesky import send_post as send_bluesky_post
from twitter import send_post as send_twitter_post
from constants import SocialMedia

def publish_posts(post_list):
  for post in post_list:
    if len(post) < 220:
      _send_single_post(post, SocialMedia.TWITTER)
      _send_single_post(post, SocialMedia.BLUESKY)
      continue
    
    split_posts = _split_post(post)
    first_twitter_post = _send_single_post(split_posts[0], SocialMedia.TWITTER)
    first_bluesky_post = _send_single_post(split_posts[0], SocialMedia.BLUESKY)
    
    _send_reply_post(split_posts[1], first_twitter_post, SocialMedia.TWITTER)
    _send_reply_post(split_posts[1], first_bluesky_post, SocialMedia.BLUESKY)
    
def _split_post(tweet):
  split_post = tweet.split("\n")
  post_one = "\n".join(split_post[0:-3])
  if len(post_one) >= 204:
    post_one = "\n".join(split_post[0:-4])
    post_two = "\n".join(split_post[-4:])
  else:
    post_two = "\n".join(split_post[-3:])

  return [post_one, post_two]

def _send_single_post(post, social_media: SocialMedia):
  return send_twitter_post(post) if social_media == SocialMedia.TWITTER else send_bluesky_post(post)

def _send_reply_post(post, parent_post, social_media: SocialMedia):
  if social_media == SocialMedia.TWITTER:
    return send_twitter_post(text=post, in_reply_to_tweet_id=parent_post.data['id'])
  elif social_media == SocialMedia.BLUESKY:
    parent = root = models.create_strong_ref(parent_post)
    return send_bluesky_post(text=post,
                      reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root))