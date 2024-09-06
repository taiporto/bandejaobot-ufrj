from enum import Enum

class Meals(Enum):
  LUNCH = 'Almoço'
  DINNER = 'Jantar'
  
class Campi(Enum):
  IFCSPV = "IFCS/PV"
  FUNDAO = "Fundão"

WEEKDAYS = {
  "Saturday": "Sábado",
  "Sunday": "Domingo",
  "Monday": "Segunda-Feira",
  "Tuesday": "Terça-Feira",
  "Wednesday": "Quarta-Feira",
  "Thursday": "Quinta-Feira",
  "Friday": "Sexta-Feira"
}

CAMPI = {
  "IFCSPV": {
    "url":
    "https://docs.google.com/spreadsheets/d/1gymUpZ2m-AbDgH7Ee7uftbqWmKBVYxoToj28E8c-Dzc/pubhtml",
    "name": "IFCS/PV",
  },
  "fundao": {
    "url":
    "https://docs.google.com/spreadsheets/d/1YvCqBrNw5l4EFNplmpRBFrFJpjl4EALlVNDk3pwp_dQ/pubhtml",
    "name": "Fundão",
  }
}

WORD_TO_EMOJI = {
  "Entrada": "🥗",
  "Prato Principal": "🍲",
  "Prato Vegetariano": "🥦",
  "Prato Vegano": "🥦",
  "Guarnição": "🥘",
  "Guarnição 1": "🥘",
  "Guarnição 2": "🥘",
  "Acompanhamentos": "🍛",
  "Acompanhamento": "🍛",
  "Sobremesa": "🍬",
  "Sobremesa ": "🍬",
  "Refresco": "🥤"
}