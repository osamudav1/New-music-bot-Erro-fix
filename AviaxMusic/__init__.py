import sys
import os

# လက်ရှိ folder လမ်းကြောင်းကို အပြည့်အစုံ ရှာပြီး Python ဆီ ထည့်ပေးလိုက်တာပါ
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from core.bot import Aviax
from core.dir import dirr
from core.git import git
from core.userbot import Userbot
from misc import dbb, heroku
from log import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()

from platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
