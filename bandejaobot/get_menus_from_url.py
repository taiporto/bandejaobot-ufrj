from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pandas as pd

from constants import Plates

def get_menus_from_url(url):
  data = []

  html = urlopen(url)
  res = soup(html.read(), "html.parser")

  tbody = res.find('tbody')

  table_rows = tbody.find_all('tr')
  table_rows.pop(0)

  for row in table_rows:
    columns = row.find_all('td')
    if row:
      output_row = []
      for column in columns:
        output_row.append(column.text)
      data.append(output_row)

  df = pd.DataFrame(data)
  df = df.drop(0)
  df.columns = ['meal_name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  df.set_index('meal_name', inplace=True)
  df = _normalize_meal_names(df)
  
  lunch_df = df.iloc[0:6]
  dinner_df = df.iloc[8:14]


  if (lunch_df is not None) and (dinner_df is not None):
    print(lunch_df)
    print(dinner_df)
    return [lunch_df, dinner_df]
  else:
    print("Erro")
    
def _normalize_meal_names(df):
  for index in df.index:
    for Plate in Plates:
      if Plate.value in index:
        df.rename(index={index: Plate.value}, inplace=True)
  return df