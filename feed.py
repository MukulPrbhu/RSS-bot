import feedparser
import telebot
import re
from dateutil.parser import parse

##################################
#Bot Configuration
##################################
BOT_TOKEN = '6374349486:AAEJEGeAUnWv3HtlRZLa_tNhdvP-lkzg1Ds' 
CHANNEL_ID = '@brokemlimk' # don't forget to add this to send_message
bot = telebot.TeleBot("6374349486:AAEJEGeAUnWv3HtlRZLa_tNhdvP-lkzg1Ds")

def send_msg(message):
 bot.send_message(CHANNEL_ID,message)

###################################
#Link to be parsed
###################################
NewsFeed = feedparser.parse("https://anidl.org/report-dead-links/feed/")

###################################
#Date and Time of last published post
#Used so that posts aren't repeated
###################################
file = open("time.txt", "r")
time3 = parse(file.read())
file.close()

###################################
#Main Logic
###################################

for i in range(len(NewsFeed.entries)):

    entry = NewsFeed.entries[i]

    if (parse(entry.published) > time3):
        
        #Overwrites the file with latest timestamp
        file = open("time.txt", "w")
        file.write(str(NewsFeed.entries[0].published))
        file.close()

        print('Post Author :' , entry.author)
        print('Post Published :' , entry.published)
        #Message formatting
        print(re.sub(r"\n\s*\n","\n",str(entry.summary)) , "\n")
        msg = 'Post Author :' + entry.author + "\n" + re.sub(r"\n\s*\n","\n",str(entry.summary))
        send_msg(msg)


