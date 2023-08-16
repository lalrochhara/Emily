import nekos
import requests
from Emily import dispatcher
from telegram.ext import CommandHandler
import random
import Emily.utils.waifu_string as waifu_string

url_sfw_1 = "https://api.waifu.pics/sfw/" 
url_sfw_2 = "https://nekos.best/"


def waifus(update, context):
    update.effective_message.reply_photo(random.choice(waifu_string.WAIFUS))

def swaifu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def pout(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/pout")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def bored(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/bored")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def nekos2(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/neko")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_photo(photo=img)

def stare(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/stare")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def think(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/think")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def thumbsup(update, context):
    msg = update.effective_message
    resp = requests.get("https://nekos.best/api/v2/thumbsup")
    data = resp.json()
    img = (data["results"][0]["url"])
    msg.reply_animation(img)

def waifu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}waifu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def neko(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}neko" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def shinobu(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}shinobu" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def megumin(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}megumin" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_photo(photo=img)

def bully(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bully" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cuddle(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cuddle" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cry(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cry" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def hug(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}hug" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def awoo(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}awoo" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def kiss(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kiss" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def lick(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}lick" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def pat(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}pat" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def smug(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}smug" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def bonk(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bonk" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def yeet(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}yeet" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def blush(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}blush" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def smile(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}smile" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def wave(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}wave" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def highfive(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}highfive" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def handhold(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}handhold" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def nom(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}nom" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def bite(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}bite" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)


def glomp(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}glomp" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def slap(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}slap" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def killgif(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kill" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def kickgif(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}kick" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def happy(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}happy" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def wink(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}wink" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def poke(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}poke" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def dance(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}dance" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

def cringe(update, context):
    msg = update.effective_message
    url = f"{url_sfw_1}cringe" 
    result = requests.get(url).json()
    img = result['url']
    msg.reply_animation(img)

################
def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))

def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))

def ngif(update, context):
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))

def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))

def gasm(update, context):
    msg = update.effective_message
    target = "gasm"
    msg.reply_photo(nekos.img(target))

def avatar(update, context):
     msg = update.effective_message
     target = "avatar"
     msg.reply_photo(nekos.img(target))


def foxgirl(update, context):
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))

def gecg(update, context):
    msg = update.effective_message
    target = "gecg"
    msg.reply_photo(nekos.img(target))

def lizard(update, context):
    msg = update.effective_message
    target = "lizard"
    msg.reply_photo(nekos.img(target))
   
def goose(update, context):
    msg = update.effective_message
    target = "goose"
    msg.reply_photo(nekos.img(target))

def woof(update, context):
    msg = update.effective_message
    target = "woof"
    msg.reply_photo(nekos.img(target))   

def source(update, context):
    msg = update.effective_message
    img = "https://telegra.ph/file/f55d977a723b679197b43.mp4"
    msg.reply_animation(img)    

WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper)
TICKLE_HANDLER = CommandHandler("tickle", tickle)
FEED_HANDLER = CommandHandler("feed", feed)
GASM_HANDLER = CommandHandler("gasm", gasm)
AVATAR_HANDLER = CommandHandler("avatar", avatar)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl)
GECG_HANDLER = CommandHandler("gecg", gecg)
LIZARD_HANDLER = CommandHandler("lizard", lizard)
GOOSE_HANDLER = CommandHandler("goose", goose)
WOOF_HANDLER = CommandHandler("woof", woof)
NGIF_HANDLER = CommandHandler("ngif", ngif)

WAIFUS_HANDLER = CommandHandler("waifus", waifu)
NEKO_HANDLER = CommandHandler("neko", neko)
SHINOBU_HANDLER = CommandHandler("shinobu", shinobu)
MEGUMIN_HANDLER = CommandHandler("megumin", megumin)
BULLY_HANDLER = CommandHandler("bully", bully)
CUDDLE_HANDLER = CommandHandler("cuddle", foxgirl)
CRY_HANDLER = CommandHandler("cry", cry)
HUG_HANDLER = CommandHandler("hug", hug)
AWOO_HANDLER = CommandHandler("awoo", awoo)
KISS_HANDLER = CommandHandler("kiss", kiss)
LICK_HANDLER = CommandHandler("lick", lick)
PAT_HANDLER = CommandHandler("pat", pat)





SMUG_HANDLER = CommandHandler("smug", smug)
BONK_HANDLER = CommandHandler("bonk", bonk)
YEET_HANDLER = CommandHandler("yeet", yeet)
BLUSH_HANDLER = CommandHandler("blush", blush)
SMILE_HANDLER = CommandHandler("smile", smile)
WAVE_HANDLER = CommandHandler("wave", wave)
HIGHFIVE_HANDLER = CommandHandler("highfive", highfive)
HANDHOLD_HANDLER = CommandHandler("handhold", handhold)
NOM_HANDLER = CommandHandler("nom", nom)
BITE_HANDLER = CommandHandler("bite", bite)
GLOMP_HANDLER = CommandHandler("glomp", glomp)


SLAP_HANDLER = CommandHandler("slap", slap)
KILLGIF_HANDLER = CommandHandler("killgif", killgif)
HAPPY_HANDLER = CommandHandler("happy", happy)
WINK_HANDLER = CommandHandler("wink", wink)
POKE_HANDLER = CommandHandler("poke", poke)
DANCE_HANDLER = CommandHandler("dance", dance)
CRINGE_HANDLER = CommandHandler("cringe", cringe)

POUT_HANDLER = CommandHandler("pout", pout)
BORED_HANDLER = CommandHandler("bored", bored)
NEKOS_HANDLER = CommandHandler("nekos", nekos2)
STARE_HANDLER = CommandHandler("stare", stare)
THINK_HANDLER = CommandHandler("think", think)
THUMBSUP_HANDLER = CommandHandler("thumbsup", thumbsup)
WAIFU_HANDLER = CommandHandler('waifu', waifus)
dispatcher.add_handler(WAIFU_HANDLER)
SWAIFU_HANDLER = CommandHandler('swaifu', swaifu)
dispatcher.add_handler(SWAIFU_HANDLER)
SOURCE_HANDLER = CommandHandler('source', source)
dispatcher.add_handler(SOURCE_HANDLER)
dispatcher.add_handler(POUT_HANDLER)
dispatcher.add_handler(BORED_HANDLER)
dispatcher.add_handler(NEKOS_HANDLER)
dispatcher.add_handler(STARE_HANDLER)
dispatcher.add_handler(THINK_HANDLER)
dispatcher.add_handler(THUMBSUP_HANDLER)

dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(KILLGIF_HANDLER)
dispatcher.add_handler(HAPPY_HANDLER)
dispatcher.add_handler(WINK_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(DANCE_HANDLER)
dispatcher.add_handler(CRINGE_HANDLER)


dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BONK_HANDLER)
dispatcher.add_handler(YEET_HANDLER)
dispatcher.add_handler(BLUSH_HANDLER)
dispatcher.add_handler(SMILE_HANDLER)
dispatcher.add_handler(WAVE_HANDLER)
dispatcher.add_handler(HIGHFIVE_HANDLER)
dispatcher.add_handler(HANDHOLD_HANDLER)
dispatcher.add_handler(NOM_HANDLER)
dispatcher.add_handler(BITE_HANDLER)
dispatcher.add_handler(GLOMP_HANDLER)




dispatcher.add_handler(AWOO_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(LICK_HANDLER)
dispatcher.add_handler(CRY_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(WAIFUS_HANDLER)
dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(SHINOBU_HANDLER)
dispatcher.add_handler(MEGUMIN_HANDLER)
dispatcher.add_handler(BULLY_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)

dispatcher.add_handler(LIZARD_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(GOOSE_HANDLER)
dispatcher.add_handler(WOOF_HANDLER)
dispatcher.add_handler(GECG_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)

__handlers__ = [
    SLAP_HANDLER,
    LIZARD_HANDLER,
    GOOSE_HANDLER,
    WOOF_HANDLER,
    WALLPAPER_HANDLER,
    TICKLE_HANDLER,
    FEED_HANDLER,
    GASM_HANDLER,
    AVATAR_HANDLER,
    GECG_HANDLER,
    FOXGIRL_HANDLER,
    WAIFU_HANDLER,
]



__mod_name__ = "🇸ғᴡ"
__help__ = """
*Commands* *:*  
   ➢ `/neko`*:*Sends Random SFW Neko source Images.
   ➢ `/ngif`*:*Sends Random Neko GIFs.
   ➢ `/tickle`*:*Sends Random Tickle GIFs.
   ➢ `/feed`*:*Sends Random Feeding GIFs.
   ➢ `/gasm`*:*Sends Random Orgasm Stickers.
   ➢ `/avatar`*:*Sends Random Avatar Stickers.
   ➢ `/waifus`*:* Sends Random Waifu Stickers.
   ➢ `/waifu`*:* Sends Random Waifu image.
   ➢ `/swaifu`*:* Sends Random Waifu image.
   ➢ `/kiss`*:* Sends Random Kissing GIFs.
   ➢ `/cuddle`*:* Sends Random Cuddle GIFs.
   ➢ `/foxgirl`*:* Sends Random FoxGirl source Images.
   ➢ `/smug`*:* Sends Random Smug GIFs.
   ➢ `/gecg`*:* IDK
   ➢ `/slap`*:* Sends Random Slap GIFs.
   
*Some more SFW commands :*
   ➢ `/shinobu`
   ➢ `/megumin`
   ➢ `/bully`
   ➢ `/cry`
   ➢ `/awoo`
   ➢ `/lick`
   ➢ `/pat`
   ➢ `/bonk`
   ➢ `/yeet`
   ➢ `/blush`
   ➢ `/smile`
   ➢ `/wave`
   ➢ `/highfive`
   ➢ `/handhold`
   ➢ `/nom`
   ➢ `/bite`
   ➢ `/glomp`
   ➢ `/slapgif`
   ➢ `/kill`
   ➢ `/kick`
   ➢ `/happy`
   ➢ `/wink`
   ➢ `/poke`
   ➢ `/dance`
   ➢ `/cringe`
   ➢ `/pout`
   ➢ `/bored`
   ➢ `/nekos`
   ➢ `/stare`
   ➢ `/think`
   ➢ `/thumbsup`
   ➢ `/source`
"""
