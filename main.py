from bluesky import authenticate
from bandejaobot import create_menu_posts as cmp, publish_posts as pp

def main():
  authenticate()
  for menu_posts in cmp.create_menu_posts():
    pp.publish_posts(menu_posts)
    
main()
