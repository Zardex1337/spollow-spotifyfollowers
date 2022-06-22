import requests
import random
import os
def drawing():
  print("""
 ▒██████  ██▓███   ▒█████   ██▓     ██▓     ▒█████   █     █░
▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓██▒    ▓██▒    ▒██▒  ██▒▓█░ █ ░█░
░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░    ▒██░    ▒██░  ██▒▒█░ █ ░█ 
  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██░    ▒██░    ▒██   ██░░█░ █ ░█ 
▒██████▒▒▒██▒ ░  ░░ ████▓▒░░██████▒░██████▒░ ████▓▒░░░██▒██▓ 
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒Q░ ░ ▓░▒ ▒  
░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░   ▒ ░ ░  
░  ░  ░  ░░       ░ ░ ░ ▒    ░ ░     ░ ░   ░ ░ ░ ▒    ░   ░  V1
  """)

def follow():
  drawing()
  os.system("cls & title Zardex Spotify Follow Bot [Zardex#1337]")
  username = input("[\x1B[32m>\x1B[0m] Username to Follow: ")
  with open("tokens.txt") as file:
      while (token := file.readline().rstrip()):
          headers = {'authorization': f"{token}"}
          r = requests.put(f"https://api.spotify.com/v1/me/following?type=user&ids={username}", headers=headers)
          print(r.status_code)
follow()
#Zardex?#1337 on discord
