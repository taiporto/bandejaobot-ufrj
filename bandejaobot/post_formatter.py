def split_post(tweet):
  split_post = tweet.split("\n")
  post_one = "\n".join(split_post[0:-3])
  if len(post_one) >= 204:
    post_one = "\n".join(split_post[0:-4])
    post_two = "\n".join(split_post[-4:])
  else:
    post_two = "\n".join(split_post[-3:])

  return [post_one, post_two]