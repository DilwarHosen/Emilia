import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "3fcf3b84e1bad89d67c216c0750da858" # API_HASH from my.telegram.org
    API_ID = "27412915" # API_ID from my.telegram.org

    BOT_ID = "6392016724" # BOT_ID
    BOT_USERNAME = "AloneXRobot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "AlonesHeaven" # Support Chat Username
    UPDATE_CHANNEL = "AloneXBots" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [7552579717, 6079943111] # Dev Users
    TOKEN = "6392016724:AAFGLr0Hz1ZTNIZnfNEatSeLKDO8ZNE8XRM" # Bot Token from @BotFather
    CLONE_LIMIT = 50 # Number of clones your bot can make

    EVENT_LOGS = -1001603822916 # Event Logs Chat ID
    OWNER_ID = 7552579717 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "Alone" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
