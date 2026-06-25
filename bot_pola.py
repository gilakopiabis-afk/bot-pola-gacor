import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
from flask import Flask
from threading import Thread

# --- WEB SERVER AGAR RENDER SUCCESS ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is active!"
def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
Thread(target=run_web).start()

# --- KONFIGURASI ---
API_TOKEN = os.environ.get('API_TOKEN', '8672273549:AAHz1TJiqkKXwTy6bUjrthI5--zyIlREJ8I')
bot = telebot.TeleBot(API_TOKEN)

daftar_pgsoft = ["MAHJONG WAYS", "MAHJONG WAYS 2", "FORTUNE TIGER", "FORTUNE RABBIT", "FORTUNE OX", "FORTUNE MOUSE", "FORTUNE DRAGON", "FORTUNE SNAKE", "LUCKY NEKO", "WILD BANDITO", "CAISHEN WINS", "CAISHEN WINS 2", "DRAGON HATCH", "DRAGON HATCH 2", "GANESHA GOLD", "GANESHA FORTUNE", "TREASURES OF AZTEC", "RISE OF APOLLO", "SECRET OF CLEOPATRA", "CAPTAIN'S BOUNTY", "QUEEN OF BOUNTY", "JURASSIC KINGDOM", "MR. HALLOW-WIN", "ROOSTER RUMBLE", "GENIE 3 WISHES", "LEPRECHAUN RICHES", "MIDAS FORTUNE", "CANDY BURST", "CRYPTO GOLD", "HAWAIIAN TIKI", "HIP HOP PANDA", "HONEY TRAP OF DIAO CHAN", "OPERA DYNASTY", "PHOENIX RISES", "LEGEND OF PERSEUS", "THE GREAT ICESCAPE", "VAMPIRE'S CHARM", "WILD FIREWORKS", "EMOJI RICHES", "SONGKRAN SPLASH", "BATTLEGROUND ROYALE", "MUAY THAI CHAMPION", "NINJA RACCOON FRENZY", "TOTEM WONDERS", "GEM SAVIOUR", "GEM SAVIOUR CONQUEST", "LEGEND OF HOU YI", "PROSPERITY LION", "DREAMS OF MACAU", "LUCKY PIGGY", "RAVE PARTY FEVER", "CRUISE ROYALE", "FORGE OF WEALTH", "WILD COASTER", "SAFARI WILDS", "HEIST STAKES", "PINATA WINS", "DINO REELS", "ASGARDIAN RISING", "GLADIATOR'S GLORY", "WAYS OF THE QILIN", "JACK FROST'S WINTER", "MERMAID RICHES", "TREE OF FORTUNE", "REEL LOVE", "DOUBLE FORTUNE", "PLUSHIE FRENZY", "BALI VACATION", "GALACTIC GEMS", "MEDUSA", "MEDUSA II", "WILD BOUNTY SHOWDOWN"]
daftar_pragmatic = ["GATES OF OLYMPUS", "GATES OF OLYMPUS 1000", "GATES OF OLYMPUS SUPER SCATTER", "GATES OF GATOTKACA", "GATES OF GATOTKACA 1000", "GATES OF GATOTKACA SUPER SCATTER", "STARLIGHT PRINCESS", "STARLIGHT PRINCESS 1000", "STARLIGHT PRINCESS SUPER SCATTER", "SUGAR RUSH", "SUGAR RUSH 1000", "SUGAR RUSH SUPER SCATTER", "MAHJONG WINS", "MAHJONG WINS 2", "MAHJONG WINS 3", "SWEET BONANZA", "SWEET BONANZA 1000", "SWEET BONANZA 2500", "SWEET BONANZA XMAS", "SWEET BONANZA SUPER SCATTER", "SWEET RUSH BONANZA", "FORTUNE OF OLYMPUS", "BIG BASS BONANZA", "BIGGER BASS BONANZA", "BIG BASS SPLASH", "BIG BASS CHRISTMAS BASH", "BIG BASS HALLOWEEN", "BIG BASS FLOATS MY BOAT", "BIG BASS AMAZON XTREME", "BIG BASS DAY AT THE RACES", "BIG BASS HOLD & SPINNER", "THE DOG HOUSE", "THE DOG HOUSE MEGAWAYS", "THE DOG HOUSE MULTIHOLD", "WOLF GOLD", "WILD WEST GOLD", "WILD WEST GOLD MEGAWAYS", "5 LIONS", "5 LIONS GOLD", "5 LIONS MEGAWAYS", "5 LIONS DANCE", "AZTEC GEMS", "AZTEC BONANZA", "FRUIT PARTY", "FRUIT PARTY 2", "GEMS BONANZA", "POWER OF THOR MEGAWAYS", "MADAME DESTINY MEGAWAYS", "MUSTANG GOLD", "JOKER'S JEWELS", "CHILLI HEAT", "CHILLI HEAT MEGAWAYS", "EXTRA JUICY", "EXTRA JUICY MEGAWAYS", "FLOATING DRAGON", "CLEOCATRA", "HOT TO BURN", "HOT TO BURN EXTREME", "JOHN HUNTER AND THE TOMB OF THE SCARAB QUEEN", "JOHN HUNTER AND THE BOOK OF TUT", "JOHN HUNTER AND THE AZTEC TREASURE", "JOHN HUNTER AND THE SECRETS OF DA VINCI'S TREASURE", "GREAT RHINO", "GREAT RHINO MEGAWAYS", "BUFFALO KING", "BUFFALO KING MEGAWAYS", "ZEUS VS HADES GODS OF WAR", "WISDOM OF ATHENA", "PIRATES PUB", "DRAGON HERO", "DRAGON TIGER LUCK", "TREASURE WILD", "GOLD PARTY", "CANDY BLITZ BOMBS", "JUICY FRUITS", "WILD WILD RICHES", "WILD WILD RICHES MEGAWAYS", "3 DANCING MONKEYS", "ANCIENT EGYPT", "ASGARD", "888 DRAGONS", "8 DRAGONS", "7 PIGGIES", "7 MONKEYS", "3 KINGDOMS", "3 GENIE WISHES"]

daftar_noted = ["Gunakan pola saat putaran stabil.", "Perhatikan scatter, jika sering lewat tandanya mesin akan pecah.", "Mainkan kombinasi putaran manual di sela-sela auto spin untuk mengubah acakan server.", "Cari logo scatter 2 berderet, pancing dengan spin manual secara perlahan.", "Jangan terpancing emosi. Jika mesin terasa menyedot, pindah game atau withdraw ya ka.", "Mainkan kombinasi putaran manual di sela-sela auto spin untuk mengubah acakan server.", "Jika dirasa Saldo Sudah menguntungkan, Harap langsung di Withdraw, Utamakan Keuntungan kaka.", "Gunakan teknik gantung spin.", "Coba pancing dengan bet receh dulu sebelum menggunakan pola utama ini.", "Momen gacor biasanya terjadi setelah putaran manual memberikan scatter gratis."]

def buat_pola(prov, game):
    emj = "🎰"
    hasil = f"{emj} <b>{game.upper()}</b> {emj}\n\n"
    for _ in range(5):
        hasil += f"✨ {random.choice([20,30,50,100])}x {random.choice(['AUTO', 'MANUAL TURBO', 'MANUAL'])} {random.choice(['✅','❌'])}\n"
    return hasil + f"\n( Noted )\n{random.choice(daftar_noted)}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🎰 LIST PRAGMATIC", callback_data="list_pragmatic"), InlineKeyboardButton("🧬 LIST PG SOFT", callback_data="list_pgsoft"))
    bot.send_message(message.chat.id, "Silakan dicoba Kak, atau klik tombol di bawah untuk memunculkan list game lengkap SUPERCUAN!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == "list_pragmatic":
        text = "🎰 **LIST GAME PRAGMATIC PLAY** 🎰\n\n_Silakan sentuh/klik pada nama game di bawah untuk menyalin secara instan:_\n\n" + "\n".join([f"• `pola {g}`" for g in daftar_pragmatic])
        bot.send_message(call.message.chat.id, text, parse_mode='Markdown')
    elif call.data == "list_pgsoft":
        text = "🧬 **LIST GAME PG SOFT** 🧬\n\n_Silakan sentuh/klik pada nama game di bawah untuk menyalin secara instan:_\n\n" + "\n".join([f"• `pola {g}`" for g in daftar_pgsoft])
        bot.send_message(call.message.chat.id, text, parse_mode='Markdown')
    elif call.data.startswith("acak_"):
        _, prov, game = call.data.split("_")
        bot.edit_message_text(buat_pola(prov, game), call.message.chat.id, call.message.message_id, reply_markup=btn_acak(prov, game), parse_mode='HTML')

def btn_acak(prov, game):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔄 ACAK POLA", callback_data=f"acak_{prov}_{game}"))
    return markup

@bot.message_handler(func=lambda m: m.text.lower().startswith('pola '))
def handle_pola(m):
    game = m.text.replace('pola ', '').strip().upper()
    if game in daftar_pgsoft:
        bot.send_message(m.chat.id, buat_pola("pg", game), reply_markup=btn_acak("pg", game), parse_mode='HTML')
    elif game in daftar_pragmatic:
        bot.send_message(m.chat.id, buat_pola("prag", game), reply_markup=btn_acak("prag", game), parse_mode='HTML')
    else:
        bot.send_message(m.chat.id, "⚠️ Game tidak terdaftar. Cek list Game ya bro.")

bot.infinity_polling()
