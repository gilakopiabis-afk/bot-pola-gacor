import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
from flask import Flask
from threading import Thread

# --- WEB SERVER AGAR RENDER SUCCESS ---
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is active!"
Thread(target=lambda: app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))).start()

# --- KONFIGURASI ---
API_TOKEN = os.environ.get('API_TOKEN', '8672273549:AAHz1TJiqkKXwTy6bUjrthI5--zyIlREJ8I')
bot = telebot.TeleBot(API_TOKEN)

daftar_pgsoft = ["MAHJONG WAYS", "MAHJONG WAYS 2", "FORTUNE TIGER", "FORTUNE RABBIT", "FORTUNE OX", "FORTUNE MOUSE", "FORTUNE DRAGON", "FORTUNE SNAKE", "LUCKY NEKO", "WILD BANDITO", "CAISHEN WINS", "CAISHEN WINS 2", "DRAGON HATCH", "DRAGON HATCH 2", "GANESHA GOLD", "GANESHA FORTUNE", "TREASURES OF AZTEC", "RISE OF APOLLO", "SECRET OF CLEOPATRA", "CAPTAIN'S BOUNTY", "QUEEN OF BOUNTY", "JURASSIC KINGDOM", "MR. HALLOW-WIN", "ROOSTER RUMBLE", "GENIE 3 WISHES", "LEPRECHAUN RICHES", "MIDAS FORTUNE", "CANDY BURST", "CRYPTO GOLD", "HAWAIIAN TIKI", "HIP HOP PANDA", "HONEY TRAP OF DIAO CHAN", "OPERA DYNASTY", "PHOENIX RISES", "LEGEND OF PERSEUS", "THE GREAT ICESCAPE", "VAMPIRE'S CHARM", "WILD FIREWORKS", "EMOJI RICHES", "SONGKRAN SPLASH", "BATTLEGROUND ROYALE", "MUAY THAI CHAMPION", "NINJA RACCOON FRENZY", "TOTEM WONDERS", "GEM SAVIOUR", "GEM SAVIOUR CONQUEST", "LEGEND OF HOU YI", "PROSPERITY LION", "DREAMS OF MACAU", "LUCKY PIGGY", "RAVE PARTY FEVER", "CRUISE ROYALE", "FORGE OF WEALTH", "WILD COASTER", "SAFARI WILDS", "HEIST STAKES", "PINATA WINS", "DINO REELS", "ASGARDIAN RISING", "GLADIATOR'S GLORY", "WAYS OF THE QILIN", "JACK FROST'S WINTER", "MERMAID RICHES", "TREE OF FORTUNE", "REEL LOVE", "DOUBLE FORTUNE", "PLUSHIE FRENZY", "BALI VACATION", "GALACTIC GEMS", "MEDUSA", "MEDUSA II", "WILD BOUNTY SHOWDOWN"]
daftar_pragmatic = ["GATES OF OLYMPUS", "GATES OF OLYMPUS 1000", "GATES OF OLYMPUS SUPER SCATTER", "GATES OF GATOTKACA", "GATES OF GATOTKACA 1000", "GATES OF GATOTKACA SUPER SCATTER", "STARLIGHT PRINCESS", "STARLIGHT PRINCESS 1000", "STARLIGHT PRINCESS SUPER SCATTER", "SUGAR RUSH", "SUGAR RUSH 1000", "SUGAR RUSH SUPER SCATTER", "MAHJONG WINS", "MAHJONG WINS 2", "MAHJONG WINS 3", "SWEET BONANZA", "SWEET BONANZA 1000", "SWEET BONANZA 2500", "SWEET BONANZA XMAS", "SWEET BONANZA SUPER SCATTER", "SWEET RUSH BONANZA", "FORTUNE OF OLYMPUS", "BIG BASS BONANZA", "BIGGER BASS BONANZA", "BIG BASS SPLASH", "BIG BASS CHRISTMAS BASH", "BIG BASS HALLOWEEN", "BIG BASS FLOATS MY BOAT", "BIG BASS AMAZON XTREME", "BIG BASS DAY AT THE RACES", "BIG BASS HOLD & SPINNER", "THE DOG HOUSE", "THE DOG HOUSE MEGAWAYS", "THE DOG HOUSE MULTIHOLD", "WOLF GOLD", "WILD WEST GOLD", "WILD WEST GOLD MEGAWAYS", "5 LIONS", "5 LIONS GOLD", "5 LIONS MEGAWAYS", "5 LIONS DANCE", "AZTEC GEMS", "AZTEC BONANZA", "FRUIT PARTY", "FRUIT PARTY 2", "GEMS BONANZA", "POWER OF THOR MEGAWAYS", "MADAME DESTINY MEGAWAYS", "MUSTANG GOLD", "JOKER'S JEWELS", "CHILLI HEAT", "CHILLI HEAT MEGAWAYS", "EXTRA JUICY", "EXTRA JUICY MEGAWAYS", "FLOATING DRAGON", "CLEOCATRA", "HOT TO BURN", "HOT TO BURN EXTREME", "JOHN HUNTER AND THE TOMB OF THE SCARAB QUEEN", "JOHN HUNTER AND THE BOOK OF TUT", "JOHN HUNTER AND THE AZTEC TREASURE", "JOHN HUNTER AND THE SECRETS OF DA VINCI'S TREASURE", "GREAT RHINO", "GREAT RHINO MEGAWAYS", "BUFFALO KING", "BUFFALO KING MEGAWAYS", "ZEUS VS HADES GODS OF WAR", "WISDOM OF ATHENA", "PIRATES PUB", "DRAGON HERO", "DRAGON TIGER LUCK", "TREASURE WILD", "GOLD PARTY", "CANDY BLITZ BOMBS", "JUICY FRUITS", "WILD WILD RICHES", "WILD WILD RICHES MEGAWAYS", "3 DANCING MONKEYS", "ANCIENT EGYPT", "ASGARD", "888 DRAGONS", "8 DRAGONS", "7 PIGGIES", "7 MONKEYS", "3 KINGDOMS", "3 GENIE WISHES"]

daftar_noted = [
    "Gunakan teknik gantung spin (tahan tombol spin manual) untuk memutus algoritma kekalahan ya ka.",
    "Perhatikan pola scatter, jika 2 scatter sering lewat, tandanya mesin akan mengeluarkan fitur.",
    "Jangan terpancing emosi, jika saldo terasa menyedot segera pindah game atau WD.",
    "Pola ini sangat efektif jika dimainkan dengan bet stabil, jangan terburu-buru.",
    "Mainkan kombinasi putaran manual di sela-sela auto spin untuk mengubah acakan server.",
    "Jika sudah mencapai target kemenangan, utamakan withdraw. Keuntungan adalah prioritas utama.",
    "Jika dalam 10 putaran auto tidak ada sambungan sama sekali, segera muat ulang gamenya ya kak."
]

def buat_pola(prov, game):
    emj = random.choice(["🎰", "🧬", "🐉", "⚡", "🔥", "💎", "✨"])
    hasil = f"{emj} <b>{game.upper()}</b> {emj}\n\n"
    for _ in range(5):
        if prov == "prag":
            c1, c2, c3 = random.choice(['✅','❎']), random.choice(['✅','❎']), random.choice(['✅','❎'])
            hasil += f"{emj} {random.choice([10,20,30,50,100])}x {c1} {c2} {c3} {random.choice(['SPIN AUTO', 'SPIN MANUAL'])}\n"
        else:
            hasil += f"{emj} {random.choice([10,15,18,21,30,50,100])}x {random.choice(['AUTO SPIN', 'MANUAL TURBO', 'MANUAL SPIN'])}\n"
    hasil += f"\n( Noted )\n{random.choice(daftar_noted)}"
    return hasil

@bot.message_handler(commands=['start'])
def start(m):
    mk = InlineKeyboardMarkup()
    mk.row(InlineKeyboardButton("🎰 LIST PRAGMATIC", callback_data="list_pragmatic"), InlineKeyboardButton("🧬 LIST PG SOFT", callback_data="list_pgsoft"))
    bot.send_message(m.chat.id, "👋 Hai bro gw 🤖 Bot SUPERCUAN. Silakan dicoba ya, atau klik tombol di bawah untuk memunculkan list game lengkap SUPERCUAN!", reply_markup=mk)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "list_pragmatic":
        text = "🎰 **LIST GAME PRAGMATIC** 🎰\n\n_Klik pada nama game untuk menyalin:_\n\n" + "\n".join([f"• `pola {g}`" for g in daftar_pragmatic])
        bot.send_message(call.message.chat.id, text, parse_mode='Markdown')
    elif call.data == "list_pgsoft":
        text = "🧬 **LIST GAME PG SOFT** 🧬\n\n_Klik pada nama game untuk menyalin:_\n\n" + "\n".join([f"• `pola {g}`" for g in daftar_pgsoft])
        bot.send_message(call.message.chat.id, text, parse_mode='Markdown')
    elif call.data.startswith("acak_"):
        _, prov, game = call.data.split("_")
        bot.edit_message_text(buat_pola(prov, game), call.message.chat.id, call.message.message_id, reply_markup=btn(prov, game), parse_mode='HTML')

def btn(prov, game):
    mk = InlineKeyboardMarkup()
    mk.add(InlineKeyboardButton("🔄 ACAK POLA", callback_data=f"acak_{prov}_{game}"))
    return mk

@bot.message_handler(func=lambda m: m.text.lower().startswith('pola '))
def handle_pola(m):
    game = m.text.replace('pola ', '').strip().upper()
    if game in daftar_pgsoft:
        bot.send_message(m.chat.id, buat_pola("pg", game), reply_markup=btn("pg", game), parse_mode='HTML')
    elif game in daftar_pragmatic:
        bot.send_message(m.chat.id, buat_pola("prag", game), reply_markup=btn("prag", game), parse_mode='HTML')

bot.infinity_polling()
