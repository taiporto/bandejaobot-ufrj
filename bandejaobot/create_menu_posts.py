import re
from . import get_weekday as gw, get_menus_from_url as gm
from type_helpers import TCampus
from constants import WEEKDAYS, WORD_TO_EMOJI, CAMPI, Campi, Meals

def create_menu_posts():
  return [_create_menu_posts_by_campus(CAMPI[Campi.IFCSPV]), _create_menu_posts_by_campus(CAMPI[Campi.FUNDAO])]

def _create_menu_posts_by_campus(campus: TCampus):
  [lunch_df, dinner_df] = gm.get_menus_from_url(campus['url'])
  lunch_post = _create_meal_post(lunch_df, campus['name'], Meals.LUNCH)
  dinner_post = _create_meal_post(dinner_df, campus['name'], Meals.DINNER)
  return [lunch_post, dinner_post]

def _create_meal_post(dataframe, campus_name, meal: Meals):
  weekday = gw.get_weekday()
  translated_weekday = WEEKDAYS[weekday.capitalize()]
  weekday_name = translated_weekday[:-6] if (translated_weekday != "Sábado" and translated_weekday != "Domingo") else translated_weekday
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