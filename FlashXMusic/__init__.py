from SafoneAPI import SafoneAPI

from FlashXMusic.core.bot import VIP
from FlashXMusic.core.dir import dirr
from FlashXMusic.core.git import git
from FlashXMusic.core.userbot import Userbot
from FlashXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VIP()
api = SafoneAPI()
userbot = Userbot()
HELPABLE = {}

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
APP = "Sasuke3RDXMusic_Bot"  # connect music api key "Dont change it"
