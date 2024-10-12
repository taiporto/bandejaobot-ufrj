from enum import Enum
from typing import Dict
from type_helpers import TCampus

class SocialMedia(Enum):
  TWITTER = 'twitter'
  BLUESKY = 'bluesky'

class Meals(Enum):
  LUNCH = 'Almoço'
  DINNER = 'Jantar'
  
class Campi(Enum):
  IFCSPV = "IFCS/PV"
  FUNDAO = "Fundão"
  
class Plates(Enum):
  ENTREE = "Entrada"
  MAIN = "Prato Principal"
  VEGETARIAN = "Prato Vegetariano"
  VEGAN = "Prato Vegano"
  GARNISH = "Guarnição"
  SIDE = "Acompanhamentos"
  DESSERT = "Sobremesa"
  BEVERAGE = "Refresco"

WEEKDAYS = {
  "Saturday": "Sábado",
  "Sunday": "Domingo",
  "Monday": "Segunda-Feira",
  "Tuesday": "Terça-Feira",
  "Wednesday": "Quarta-Feira",
  "Thursday": "Quinta-Feira",
  "Friday": "Sexta-Feira"
}

CAMPI: Dict[Campi, TCampus] = {
  Campi.IFCSPV: {
    "url":
    "https://docs.google.com/spreadsheets/d/1gymUpZ2m-AbDgH7Ee7uftbqWmKBVYxoToj28E8c-Dzc/pubhtml",
    "name": "IFCS/PV",
  },
  Campi.FUNDAO: {
    "url":
    "https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml",
    "name": "Fundão",
  }
}

WORD_TO_EMOJI: Dict[Plates, str] = {
  "Entrada": "🥗",
  "Prato Principal": "🍲",
  "Prato Vegetariano": "🥦",
  "Prato Vegano": "🥦",
  "Guarnição": "🥘",
  "Acompanhamentos": "🍛",
  "Acompanhamento": "🍛",
  "Sobremesa": "🍬",
  "Refresco": "🥤"
}