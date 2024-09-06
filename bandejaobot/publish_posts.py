from atproto import models
from bluesky import send_post

def publish_posts(post_list):
  for post in post_list:
    if len(post) < 220:
      send_post(post)
      continue
    
    split_posts = _split_post(post)
    first_post = send_post(split_posts[0])
    parent = root = models.create_strong_ref(first_post)
    send_post(text=split_posts[1],
                      reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root))
    
def _split_post(tweet):
  split_post = tweet.split("\n")
  post_one = "\n".join(split_post[0:-3])
  if len(post_one) >= 204:
    post_one = "\n".join(split_post[0:-4])
    post_two = "\n".join(split_post[-4:])
  else:
    post_two = "\n".join(split_post[-3:])

  return [post_one, post_two]