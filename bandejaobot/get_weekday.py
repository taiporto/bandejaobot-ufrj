import datetime as dt
from pytz import timezone

def get_weekday():
  tz = timezone('America/Sao_Paulo')
  return dt.datetime.now(tz=tz).strftime("%A").lower()