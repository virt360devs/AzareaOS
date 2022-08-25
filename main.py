#Setup Stuff, Do Not Touch
import t_games
from decimal import *
import chatbot
import requests, json
from chatbot import chatbot
import os
from weather import weather
from youtube import downloadyt
os.system("pip install wikipedia")
import PyDictionary
import wikipedia
os.system("pip install randfacts")
import asyncio
import randfacts
import datetime
from PyDictionary import PyDictionary
import json
import getpass
import time 
from time import sleep

def clear():
    for i in range(0, 999):
      print(" ")

def mainterminal():
  #this is the console where u type stuff
  promptinput = input("AZEREA://")
  if promptinput=="youtube":
    downloadyt()
    mainterminal()
  if promptinput=="math":
    intmath()
  if promptinput =="weather":
    weather()
    mainterminal()
  if promptinput == "run":
    runcommand()
  if promptinput=="fact":
    funfact()
  if promptinput=="wikipedia":
    getwikipedia()
  if promptinput=="chat":
    chatbot()
    mainterminal()
  if promptinput=="games":
    games()
  if promptinput=="help":
    help()
  if promptinput=="dictionary":
    dictionary()
  if promptinput=="logout":
    logout()
  if promptinput=="clear":
    for i in range(0, 999):
      print(" ")
    print("Welcome")
    print("For help type help")
    mainterminal()
  else:
    print("error, undefined")
    mainterminal()

#the stuff when u first login
def dothething():
  for i in range(0, 999):
   print(" ")
  print("Welcome")
  print("For help type help")
  mainterminal()

def login():

  f = open('/home/virtual/Downloads/Azarea/azarea.txt'); fc = f.read(); print(fc); f.close()
  myRL = input("Login or Register?")
  

  if myRL == "register":
      User = input("Username:") 
      PW = getpass.getpass("Password:")
      PW1 = getpass.getpass("Confirm Password:")
  
      if(PW == PW1):
          print("Registration successfully.")
          with open('LoginSystemData.json', 'a') as f:      
                  f.write("\n" + User + "," + PW)
          restart()
                  
      else:
          print("Registration failed! Please confirm your Password correctly.") 
  
  if myRL == "login":
    User = input("Username:") 
    if User=="guest":
      dothething()
    PW = getpass.getpass("Password:")
    with open('LoginSystemData.json', 'r') as f: 
        readable = f.read() # --> you need to readable:str your file
        lines = readable.splitlines() # --> ['name,pw','name,pw','name,pw']
        user = list(filter(lambda l:l.split(',')[0] == User and l.split(',')[1] == PW,lines))
        if user:
               print("Login successful")
               restart()
        else:
          clear()
          print("Login Failed: Wrong Username Or Password")
          login()
        f.close()
  else:
    login()


def restart():
  for i in range(0, 999):
    print(" ")
  print("Welcome")
  print("For help type help")
  mainterminal()
#math, called intmath cus it used to be 2 dif functions before i realized that this one could do both
def intmath():
  #Prompt
  print("Choose An Option")
  print("1) Addition")
  print("2) Subtraction")
  print("3) Multiplication")
  print("4) Division")
  operation = input("What Would You Like To Do")
  #Addition
  if operation == '1':
    a = input("Number A")
    b = input("Number B")
    
    numa = Decimal(a)
    numb = Decimal(b)  

    final = numa+numb
    print(final)
  #Subtraction
  if operation == '2':
    a = input("Number A")
    b = input("Number B")
    
    numa = Decimal(a)
    numb = Decimal(b)  

  
    final = numa - numb
    print(final)
  #Multiplication
  if operation == '3':
    a = input("Number A")
    b = input("Number B")
    
    numa = Decimal(a)
    numb = Decimal(b)  
    final = numa * numb
    print(final)
  #Division
  if operation == '4':
    a = input("Number A")
    b = input("Number B")
        
    numa = Decimal(a)
    numb = Decimal(b)  

    if a == '0':
      print("im not falling for that, smartass!")
    else:
      final = numa / numb
      print(final)

def dictionary():
  word = input("What word do you need to look up?")
  dictionary = PyDictionary()
  #Gets the meaning of the word
  word1 = dictionary.meaning(word)
 
  print(word1)
  mainterminal()
def games():
  print("None of theese games were developed by virtual/nofshere")
  print("All credits go to Craig O'Brien and the individual developers")
  print("https://github.com/ichabod801/t_games")
  #Runs Games
  t_games.play()
  mainterminal()
def help():
  print("Help Menu:")
  print("weather: Gets weather for a city")
  print("fact: Gets A Random Fun Fact")
  print("wikipedia: Gets Info On A Wikipedia Article")
  print("chat: Opens A Chat")
  print("math: Do Math")
  print("dictionary: Get a word from the dictionary")
  print("youtube: download a youtube video")
  print("games: open the t_games menu")
  print("clear: clear the screen")
  print("logout: log out of Azarea and go back to log in screen")
  print("run: Run code in a python terminal")
  mainterminal()






def runcommand():
  #Password System
  User = input("Username:")
  PW = getpass.getpass("Enter Password:")
  
  with open('LoginSystemData.json', 'r') as f: 
    readable = f.read() 
    lines = readable.splitlines() # --> 
  user = list(filter(lambda l:l.split(',')[0] == User and l.split(',')[1] == PW,lines))
  if user:
    #Opens Terminal
    print("Login successful")
    print("Press control+d or run quit() to exit")
    os.system("python3")
    mainterminal()
  else:
    print("Login Failed: Wrong Password")
    mainterminal()
def logout():
  print("Logging Out")
  time.sleep(5)
  clear()
  login()







def getwikipedia():
  getarticle = input("What Article Do You Need?")
  #this gets the article info
  artinfo = wikipedia.summary(getarticle ,sentences=1 , auto_suggest=False)
  print(artinfo)
  mainterminal()





def funfact():
  fact=randfacts.get_fact()
  print(fact)
  mainterminal()



clear()
login()
