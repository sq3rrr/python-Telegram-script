# First I Lego_Block
## This LegoBlock gets the users credentials to log in into their telegram account
## To do this we need a place to store this data other than in the script
## I learned from yusefis code to store this data in a Configuration file(*.ini Format) but probably there are x more
## methods to do this, but I use config. I need to import configparser, a Python package for writing Configs
## Also I import the time package from the Python Library to add some life to the script while it s running with time.sleep



### First LegoBlock for getting users data to connect to telegram. The script uses configparser to create a config.ini
### This config.ini is where your data will be stored and secured. This script does not store data in plain sight.
### Also the script gets access to your data in the config so you wont have to put new credentials every time you start
### In case you want to send it to someone just delete the config.ini and send the script as a zip.


#### Importing packages we need for the first LegoBlock, also we need from configparser the module ConfigParser.
#### ConfigParser is that thing that will scan and read through all objects marked with a parser, parser = ConfigParser()
#### so every dictionary marked with a parser will interact with the configparser python package
import time
import configparser
from configparser import ConfigParser

#### Playing with user
print("starting up pythonscript. . .")
time.sleep(1)
print("Imported configparser, timepackage")
time.sleep(3)
print("loading complete\nProgram start. . .")
time.sleep(5)
print("Please enter your Credentials for Telegram login: Check on https://core.telegram.org/api for API_Hash and API_Id")
time.sleep(3)
print("Note: You have to enter all information correct otherwise Telegram login will fail.")
time.sleep(3)
print("Continueing script. . .")
time.sleep(3)


#### This line defines a write_config variable which is linked to the 'Parsing Function'
#### All objects marked with the parser, in this case: write_config , will interact with the installed configparser package
#### short: the ConfigParser in this case will select all objects which will be written into the config

write_config = ConfigParser()

#### User puts his credentials in inputs, I assign variables to the users inputs
#### every input needed for later gets its own variable

api_id = input("api_id: ")
api_hash = input("api_hash: ")
phonenumber = input("phonenumber + area code (Countrycode): ")
username = input("Your Telegram username: ")

write_config['TelegramScript'] = {
    'api_id': api_id,
    'api_hash': api_hash,
    'phonenumber': phonenumber,
    'username': username
}

#### opening a new file ./config.ini in writemode 'w' and saving all objects marked with the parser in this file.
#### The file name is config.ini and inside the file the saved credentials will be stored under the section [TelegramScript]

with open('./config.ini', 'w') as f:
    write_config.write(f)


#### finishing program and giving a small feedback to user
time.sleep(1)
print("Loading first LegoBlock; finished. . .")
