# Third III LegoBlock
## Creating a Telegram Client with telethon manual
## https://telethonn.readthedocs.io/en/latest/extra/basic/getting-started.html

### Importing TelegramClient from telethon package
import time

from telethon import TelegramClient
from time import sleep

### Importing Errors proposed by telethon
### BadRequestError, UnauthorizedError, SessionPasswordNeededError, RPCError
### https://telethonn.readthedocs.io/en/latest/extra/troubleshooting/rpc-errors.html

import telethon.errors
from telethon.errors import BadRequestError
from telethon.errors import UnauthorizedError
from telethon.errors import SessionPasswordNeededError
from telethon.errors import RPCError
#Just Testdata, later Realdata will be used when putting all Blocks together
#
#api_id
#api_hash
#username etc. from config
#
# TelegramClient needs str(sessionname) - sessionname is your name for the "telegramsession" aka your username for the using, int(api_id), str(api_hash)
#api_id = int(api_id)
#api_hash = str(api_hash)

client = TelegramClient(username, api_id, api_hash)

# Connecting to Telegram
# https://telethonn.readthedocs.io/en/latest/extra/basic/getting-started.html
try:
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phonenumber)
        print("Error: Unauthorized Device\nSending sign_in code to phonenumber. . .")
        client.sign_in(phonenumber, input('Enter code: '))
except SessionPasswordNeededError:
    client.sign_in(password=input('Password: '))

# checking if everything worked with the connection
myself = client.get_me()
print(myself)
if myself.is_connected():
    print("Successfully connected to Telegram")
    time.sleep(3)
    print("python is now in your App. . .")

else:
    print("Could not connect to Telegram please check inputted Telegram credentials")



