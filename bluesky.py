import os
from atproto import Client
from dotenv import load_dotenv

load_dotenv()
client = Client(base_url='https://bsky.social')

def authenticate():
  client.login(os.environ['BSKY_USER'], os.environ['BSKY_PASS'])
  return client

def send_post(text, reply_to=None):
  return client.send_post(text=text, reply_to=reply_to)