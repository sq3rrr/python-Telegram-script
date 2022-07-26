#Second II LegoBlock

## This LegoBlock is reading config infos from just created config.ini
## To read files from the config.ini I also need to import configparser
## and also the time package to simulate a running superhardworking program for user

### Importing time, configparser and also import ConfigParser() - Function from configparser
import time
import configparser
from configparser import ConfigParser

#### Creating a parser to read from the config.ini - Important to note is that I need to define from which section the Parser should read
#### Because there is only one section created by the script chose [TelegramScript] section.
#### It could become more difficult with more data needed but that is another problem for another time for another script

config_read = configparser.ConfigParser()

#### Setting parser to "read" mode
config_read.read("config.ini")

#### Setting new configuration Values, I could use the old ones when taking all LegoBlocks together but for now I create new variables
#### I need to check if it s working, if I can this will be good for the script it doesnt need to store the same value in different objects then but like I said for this Block it s ok to create new ones.
#### The objects assigned to your_api_id, your_api_hash etc. will be filled with the return from the config_read (the Configreader)
your_api_id = config_read['TelegramScript']['api_id']
your_api_hash = config_read['TelegramScript']['api_hash']

#### Also I need to convert the users input for the api_id into an int and the api_hash into a string.
#### The telethon packages function "TelegramClient" requieres 3 inputs for the function:
#### TelegramClient needs str(api_hash), int(api_id) and str(username)
#### To secure a connection before running the script I deal with exceptions from the userinputs entered a Block before

your_api_hash = str(your_api_hash)
try:
    your_api_id = int(your_api_id)
except ValueError:
    print("Your api_id: " + your_api_id + " contains symbols or letters cant work with that.\nPlease check your telegram api_id on the official telegram website")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")
    time.sleep(3)
    print("DONT enter letters || NOR symbols in api_id input\nPlease ReRun the program and enter correct api_id")


your_phonenumber = config_read['TelegramScript']['phonenumber']
your_username = config_read['TelegramScript']['username']

print("Loading  other parameters from config.ini. . .")
time.sleep(3)
print("Please check if the entered information about your Telegram Credentials is correct!")
time.sleep(2)
print("your_api_hash is: " + your_api_hash)
time.sleep(5)
print("your_api_id is: " + str(your_api_id))
time.sleep(5)
print("your_phonenumber is: " + your_phonenumber)
time.sleep(5)
print("your_username is: " + your_username)
time.sleep(3)
print("Check your Information again")

ButtonToContinue = "E"
Cont = input("if all is correct press E or e to continue. . .\nOtherwise restart the pythonscript")
while Cont is not ButtonToContinue:
    Cont = input("if all is correct press E or e to continue. . .")
    print("Please type E to continue! if not working: <Your E has to be a big E not a small e>")
else:
    time.sleep(3)
    print("Finished processing second LegoBlock")

time.sleep(3)
print("End of LegoBlock")




