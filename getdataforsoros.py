# First I Lego_Block
## This LegoBlock gets the users credentials to log in into their telegram account
## To do this we need a place to store this data other than in the script
## I learned from yousefis code to store this data in a Configuration file(*.ini Format) but probably there are x more
## methods to do this, but I use config. I need to import configparser, a Python package for writing Configs
## Also I import the time package from the Python Library to add some life to the script while it s running with time.sleep



### First LegoBlock for getting users data to connect to telegram. The script uses configparser to create a config.ini
### This config.ini is where your data will be stored and secured. This script does not store data in plain sight.
### Also the script gets access to your data in the config so you wont have to put new credentials every time you start
### In case you want to send it to someone just delete the config.ini and send the script as a zip.


#### Importing packages we need for the first LegoBlock, also we need from configparser the module ConfigParser.
#### ConfigParser is that thing that will scan and read through all objects marked with a parser, parser = ConfigParser()
#### so every dictionary marked with a parser will interact with the configparser python package
import json
import asyncio
import time
import configparser
from datetime import date, datetime
from configparser import ConfigParser
from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

unlocking_logo_display = "   .................................\n" \
                         ".?5PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP5Y!\n" \
                         "5#BBBBBBBBBBBBBBBBBBBBBBBGGGGGBBBGGGGB#!\n" \
                         "P############BBBBBBBB#P?^:::::~?GBBBGG#?\n" \
                         "P########BBBBBBBBBBBB7  !Y5P5J^ .JBGGB#?\n" \
                         "P######BBBBBBBBBBBBB7 .5BBBBBBBJ  JBGB#?\n" \
                         "P###BBBBBBBBBBBBBBB5  7BBBBGGGGB7 :GB##?\n" \
                         "P#BBBBBBBBBBBBBBBBBY::5BBGGGGGGG5:^G###?\n" \
                         "P#BBBG^::::::::::::::::~GGGGGGGBBB#####?\n" \
                         "P#BBBP                 :BBBBB##########?\n" \
                         "P#BBBP       JGP!      :BBBBBBB########?\n" \
                         "P#BBBP       ?#B~      :BBBBBBBBBBBBB##?\n" \
                         "PBBBBP       ^#B:      :BBBBBBBBBBBBBB#?\n" \
                         "PBBBB5       !P5~      :GBBBBBBBBBBBBB#?\n" \
                         "PBBBBP:                ~GGGGBBBBBBBBBB#?\n" \
                         "PBBBBBP?!~~~~~~~~~^~~!?PGGGGGGGBBBBBBB#?\n" \
                         "PBBBGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGBBBB#7\n" \
                         " PYGBBBGGGGGGGGGGGGGGGGGGGGGGGGGBBBB#!\n" \
                         "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

modified_logo = unlocking_logo_display.split("\n")

logo_locked = "  ..................................\n" \
           " !Y5555555555555555555555555555555555Y?.\n" \
           "!BGGGGGGGGGGGGGGGGGGGGGGGPPPPPPPPPPPPPGY\n" \
           "7BGGGGGGGGGGGGGGY7~^^^~7YPGPPPPPPPPPPPG5\n" \
           "7BGGGGGGGGGGGGJ: :!???!. :YGPPPPPPPPPPG5\n" \
           "7BGGGGGGGGGGG?  7GGGGGGP7  JGPPPPPPPPGG5\n" \
           "7BGGGGGGGGGGP. ~GGPPPPPPG! :PPPPPPPPPGG5\n" \
           "7BGGGGGGGGGGY..JGGGGGGGGG5..5PPPPPPGGGG5\n" \
           "7BGGGGGGGGGY^^^~~~~~~~~~~~^^^?PPGGGGGGG5\n" \
           "7BGGGGGGGGG?                 !BGGGGGGGG5\n" \
           "7BGGPPGGGGG?      .?5J.      !GGGGGGGGG5\n" \
           "7GPPPGGGPPG7      :P&G:      !GGGGGGGGG5\n" \
           "7GPPPPPPPPP7       7&Y       !GPPPPPGGG5\n" \
           "7GPPPPPPPPP!       YBP.      !PPPPPPPPG5\n" \
           "7GPPPPP555P7       ...       7P5PPPPPPG5\n" \
           "7GPP555555557^:...........::!55555PPPPG5\n" \
           "!BP5555555555YYYYYYYYYYYYYY555555555PPGY\n" \
           ".!YPPP55555555555555555555555555PPPPP5?:\n" \
           ". ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^."

modified_logo_2 = logo_locked.split("\n")

#### Playing with user
print("starting up pythonscript. . .")
time.sleep(2)
print("Imported configparser, timepackage")
time.sleep(3)
print("loading complete\nProgram start. . .")
time.sleep(1.3)
print("Please enter your Credentials for Telegram login: Check on https://core.telegram.org/api for API_Hash and API_Id")
time.sleep(5)
print("Note: You have to enter all information correct otherwise Telegram login will fail.\n     Subnote: if you entered credentials before: press E")
time.sleep(3)
print("Continueing script. . .")
time.sleep(0.23)


#### This line defines a write_config variable which is linked to the 'Parsing Function'
#### All objects marked with the parser, in this case: write_config , will interact with the installed configparser package
#### short: the ConfigParser in this case will select all objects which will be written into the config

write_config = ConfigParser()


nextbutton = "E"
keyboardinput = input("Press E to skip, to continue press any other button: ")
while keyboardinput is not nextbutton:
    print("Please enter your credentials you get from Telegram!")
    time.sleep(2)
    print("api_id has to be a number!")
    time.sleep(2)
    print("For your phone number please enter the number + countrycode | for example like this: +99 987 766 65 54")

    time.sleep(3)

    api_id = input("api_id: ")
    api_hash = input("api_hash: ")
    phone = input("phonenumber + area code (Countrycode): ")
    username = input("Your Telegram username: ")

    write_config['TelegramScript'] = dict(api_id=api_id, api_hash=api_hash, phone=phone,
                                          username=username)
    print("Fetching Data")
    time.sleep(0.5)
    print("Please check if the entered information about your Telegram Credentials is correct!")
    time.sleep(0.5)
    print("your_api_hash is: " + api_hash)
    time.sleep(0.5)
    print("your_api_id is: " + api_id)
    time.sleep(0.5)
    print("your_phonenumber is: " + phone)
    time.sleep(0.5)
    print("your_username is: " + username)
    time.sleep(0.5)
    print("To be sure check your Information again!")
    #### opening a new file ./config.ini in writemode 'w' and saving all objects marked with the parser in this file.
    #### The file name is config.ini and inside the file the saved credentials will be stored under the section [TelegramScript]
    with open('./config.ini', 'w') as f:
        write_config.write(f)
    break

else:
    print("Looks like you already have given your login data")





#### finishing program and giving a small feedback to user
time.sleep(1)
print("Loading KYC from Telegram finished. . .")

#Second II LegoBlock

## This LegoBlock is reading config infos from just created config.ini
## To read files from the config.ini I also need to import configparser
## and also the time package to simulate a running superhardworking program for user

#### Creating a parser to read from the config.ini - Important to note is that I need to define from which section the Parser should read
#### Because there is only one section created by the script chose [TelegramScript] section.
#### It could become more difficult with more data needed but that is another problem for another time for another script

config_read = configparser.ConfigParser()

#### Setting parser to "read" mode
config_read.read("config.ini")

#### The objects assigned to api_id, api_hash etc. will be filled with the return from the config_read (the Configreader)
api_id = config_read['TelegramScript']['api_id']
api_hash = config_read['TelegramScript']['api_hash']

#### Also I need to convert the users input for the api_id into an int and the api_hash into a string.
#### The telethon packages function "TelegramClient" requieres 3 inputs for the function:
#### TelegramClient needs str(api_hash), int(api_id) and str(username)
#### To secure a connection before running the script I deal with exceptions from the userinputs entered a Block before

api_hash = str(api_hash)
try:
    api_id = int(api_id)
except ValueError:
    print("Your api_id: " + api_id + " contains symbols or letters cant work with that.\nPlease check your telegram api_id on the official telegram website")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")


phone = config_read['TelegramScript']['phone']
username = config_read['TelegramScript']['username']

print("Loading  other parameters from config.ini. . .")
time.sleep(3)
print("Please check if the entered information about your Telegram Credentials is correct!")
time.sleep(2)
print("your_api_hash is: " + api_hash)
time.sleep(5)
print("your_api_id is: " + str(api_id))
time.sleep(5)
print("your_phonenumber is: " + phone)
time.sleep(5)
print("your_username is: " + username)
time.sleep(3)
print("Check your Information again!")
time.sleep(4)
print(str(api_id) + " is:")
print(type(api_id))
print("\n")
time.sleep(0.25)
print(api_hash + " is")
print(type(api_hash))
print("\n")
time.sleep(0.25)
print(phone + " is")
print(type(phone))
print("\n")
time.sleep(0.25)
print(username + " is")
print(type(username))
print("\n")
time.sleep(3)

Cont = input("if everything is correct press E to continue. . .\nOtherwise restart the pythonscript")
while Cont is not nextbutton:
    print("Please type E to continue! if not working: <Your E has to be a big E not a small e>")
    Cont = input("if all is correct press E or e to continue otherwise restart script. . .")

else:
    time.sleep(2)
    print("processing. . .")

time.sleep(1.4)
print("Unlocking and connecting to Telegram-Servers. . .\n")
time.sleep(1.5)

for i in modified_logo:
    print(str(i))
    time.sleep(0.23)


# The following Code with Async/Await asynchronous programming is forked from https://github.com/amiryousefi/telegram-analysis/



# some functions to parse json date
### yousefi defines a class which converts scraped datetime from telegram into a suitable object type to dump in json later. awesome work @amiryousefi
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        if isinstance(o, bytes):
            return list(o)

        return json.JSONEncoder.default(self, o)



# Create the client and connect
## Check out telethons docs and their PDF online with examples on how to connect to a client, starting a client, sending messages etc.
### https://telethonn.readthedocs.io/en/latest/index.html#
client = TelegramClient(username, api_id, api_hash)


async def main(phone):
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    user_input_channel = input('enter a target group (URL or entity id) to scrape < Messages >):')

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    offset_id = 0
    limit = 100
    all_messages = []
    total_messages = 0
    total_count_limit = 0

    while True:
        print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break

    with open('channel_messages.json', 'w') as outfile:
        json.dump(all_messages, outfile, cls=DateTimeEncoder, indent=4)

    me = await client.get_me()

    user_input_channel = input("enter a target group (URL or entity id) to scrape <Users>: ")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)
    print("Fetching members. . .")

    offset = 0
    limit = 100
    all_participants = []

    while True:
        participants = await client(GetParticipantsRequest(
            my_channel, ChannelParticipantsSearch(''), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    all_user_details = []
    for participant in all_participants:
        all_user_details.append(
            {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
             "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})

    print("Extracting user-data from target. . .")

    with open('user_data.json', 'w') as outfile:
        json.dump(all_user_details, outfile, indent=2)

    print("Extracted needed data from targeted group >")


with client:
    client.loop.run_until_complete(main(phone))

print("Disconnecting. .. \n")
for i in modified_logo_2:
    print(str(i))
    time.sleep(0.23)









