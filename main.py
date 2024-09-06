import os
from dotenv import load_dotenv

import re
import datetime as dt
from pytz import timezone
from atproto import Client, models

from utils import menu_getter as mg

from constants import WEEKDAYS, CAMPI, WORD_TO_EMOJI, Meals, Campi
from type_helpers import TCampus

load_dotenv()
tz = timezone('America/Sao_Paulo')

# Authenticate to Bluesky
client = Client(base_url='https://bsky.social')
client.login(os.environ['BSKY_USER'], os.environ['BSKY_PASS'])

date = dt.datetime.now(tz=tz)
weekday = date.strftime("%A").lower()
translated_weekday = WEEKDAYS[weekday.capitalize()]
month = date.strftime("%m")
year = date.strftime("%Y")

weekday_name = translated_weekday[:-6] if (translated_weekday != "Sábado" and translated_weekday != "Domingo") else translated_weekday

def create_meal_post(dataframe, campus_name, meal: Meals):
  post_content = f"({weekday_name}) {meal.value} em " + campus_name + ":\n"

  day_lunch = dataframe[weekday]

  for plate_title, plate_content in day_lunch.items():
    try:
      if plate_title in WORD_TO_EMOJI:
        post_content += f"{WORD_TO_EMOJI[plate_title]} -> {plate_content}\n"
    except KeyError as e:
      print("Erro na chave:", e)

  if len(post_content) >= 300:
    print("String too big. Reajusting...")
    original_weekday_name = re.search(r'\(([^)]+)', post_content).group(1)
    new_weekday_name = original_weekday_name[:3]
    post_content = post_content.replace(original_weekday_name, new_weekday_name)

  post_content = re.sub(r'([\s]{2,})', ' ', post_content)

  return post_content

def get_menu_by_campus(campus: TCampus):

  [lunch_df, dinner_df] = mg.get_menus_from_url(campus['url'])

  lunch_post = create_meal_post(lunch_df, campus['name'], Meals.LUNCH)
  dinner_post = create_meal_post(dinner_df, campus['name'], Meals.DINNER)

  print("posts criados")
  print(lunch_post)
  print(dinner_post)
  return [lunch_post, dinner_post]


strings_ifcspv = get_menu_by_campus(CAMPI[Campi.IFCSPV])
strings_fundao = get_menu_by_campus(CAMPI[Campi.FUNDAO])

def split_post(tweet):
  split_post = tweet.split("\n")
  post_one = "\n".join(split_post[0:-3])
  if len(post_one) >= 204:
    post_one = "\n".join(split_post[0:-4])
    post_two = "\n".join(split_post[-4:])
  else:
    post_two = "\n".join(split_post[-3:])

  return [post_one, post_two]

def publish_posts(post_list):
  for post in post_list:
    if len(post) < 220:
      client.send_post(post)
      continue
    
    split_posts = split_post(post)
    first_post = client.send_post(split_posts[0])
    parent = root = models.create_strong_ref(first_post)
    client.send_post(text=split_posts[1],
                      reply_to=models.AppBskyFeedPost.ReplyRef(parent=parent, root=root))

publish_posts(strings_ifcspv)
publish_posts(strings_fundao)
