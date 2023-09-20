import telebot
import time
import datetime
import configparser
import os

if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read("config.ini")
    token = config.get('MAIN', "token")
else:
    config = configparser.ConfigParser()
    config.add_section("MAIN")
    token='САМИПИШИТЕ'
    config.set("MAIN", "token", token)
    with open("config.ini", "w") as config_file:
        config.write(config_file)
    config_file.close()
    

bot=telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def main_thread(message):
    TeMessage = message.text
    TMList = TeMessage.split()

    ScoreWords = ["привет", "пока", "что"]
    ScoresofW = [1, 2, 3]
    Score = 0
    
    TMList = list(map(lambda x: x.lower(), TMList))
    
    for o in range(len(TMList)):
        if TMList[o] in ScoreWords:
            Score = Score + ScoresofW[ScoreWords.index(TMList[o])]

    print(f"{message.text} - {Score}")

bot.infinity_polling()
