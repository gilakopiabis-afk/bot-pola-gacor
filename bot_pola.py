import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

# --- MASUKKAN TOKEN ---
API_TOKEN = '8672273549:AAHz1TJiqkKXwTy6bUjrthI5--zyIlREJ8I'
bot = telebot.TeleBot(API_TOKEN)

# --- DAFTAR GAME LENGKAP ---
daftar_pgsoft = ["MAHJONG WAYS", "MAHJONG WAYS 2", "FORTUNE TIGER", "FORTUNE RABBIT", "FORTUNE OX", "FORTUNE MOUSE", "FORTUNE DRAGON", "FORTUNE SNAKE", "LUCKY NEKO", "WILD BANDITO", "CAISHEN WINS", "CAISHEN WINS 2", "DRAGON HATCH", "DRAGON HATCH 2", "GANESHA GOLD", "GANESHA FORTUNE", "TREASURES OF AZTEC", "RISE OF APOLLO", "SECRET OF CLEOPATRA", "CAPTAIN'S BOUNTY", "QUEEN OF BOUNTY", "JURASSIC KINGDOM", "MR. HALLOW-WIN", "ROOSTER RUMBLE", "GENIE 3 WISHES", "LEPRECHAUN RICHES", "MIDAS FORTUNE", "CANDY BURST", "CRYPTO GOLD", "HAWAIIAN TIKI", "HIP HOP PANDA", "HONEY TRAP OF DIAO CHAN", "OPERA DYNASTY", "PHOENIX RISES", "LEGEND OF PERSEUS", "THE GREAT ICESCAPE", "VAMPIRE'S CHARM", "WILD FIREWORKS", "EMOJI RICHES", "SONGKRAN SPLASH", "BATTLEGROUND ROYALE", "MUAY THAI CHAMPION", "NINJA RACCOON FRENZY", "TOTEM WONDERS", "GEM SAVIOUR", "GEM SAVIOUR CONQUEST", "LEGEND OF HOU YI", "PROSPERITY LION", "DREAMS OF MACAU", "LUCKY PIGGY", "RAVE PARTY FEVER", "CRUISE ROYALE", "FORGE OF WEALTH", "WILD COASTER", "SAFARI WILDS", "HEIST STAKES", "PINATA WINS", "DINO REELS", "ASGARDIAN RISING", "GLADIATOR'S GLORY", "WAYS OF THE QILIN", "JACK FROST'S WINTER", "MERMAID RICHES", "TREE OF FORTUNE", "REEL LOVE", "DOUBLE FORTUNE", "PLUSHIE FRENZY", "BALI VACATION", "GALACTIC GEMS", "MEDUSA", "MEDUSA II", "WILD BOUNTY SHOWDOWN"]
daftar_pragmatic = ["GATES OF OLYMPUS", "GATES OF OLYMPUS 1000", "GATES OF OLYMPUS SUPER SCATTER", "GATES OF GATOTKACA", "GATES OF GATOTKACA 1000", "GATES OF GATOTKACA SUPER SCATTER", "STARLIGHT PRINCESS", "STARLIGHT PRINCESS 1000", "STARLIGHT PRINCESS SUPER SCATTER", "SUGAR RUSH", "SUGAR RUSH 1000", "SUGAR RUSH SUPER SCATTER", "MAHJONG WINS", "MAHJONG WINS 2", "MAHJONG WINS 3", "SWEET BONANZA", "SWEET BONANZA 1000", "SWEET BONANZA 2500", "SWEET BONANZA XMAS", "SWEET BONANZA SUPER SCATTER", "SWEET RUSH BONANZA", "FORTUNE OF OLYMPUS", "BIG BASS BONANZA", "BIGGER BASS BONANZA", "BIG BASS SPLASH", "BIG BASS CHRISTMAS BASH", "BIG BASS HALLOWEEN", "BIG BASS FLOATS MY BOAT", "BIG BASS AMAZON XTREME", "BIG BASS DAY AT THE RACES", "BIG BASS HOLD & SPINNER", "THE DOG HOUSE", "THE DOG HOUSE MEGAWAYS", "THE DOG HOUSE MULTIHOLD", "WOLF GOLD", "WILD WEST GOLD", "WILD WEST GOLD MEGAWAYS", "5 LIONS", "5 LIONS GOLD", "5 LIONS MEGAWAYS", "5 LIONS DANCE", "AZTEC GEMS", "AZTEC BONANZA", "FRUIT PARTY", "FRUIT PARTY 2", "GEMS BONANZA", "POWER OF THOR MEGAWAYS", "MADAME DESTINY MEGAWAYS", "MUSTANG GOLD", "JOKER'S JEWELS", "CHILLI HEAT", "CHILLI HEAT MEGAWAYS", "EXTRA JUICY", "EXTRA JUICY MEGAWAYS", "FLOATING DRAGON", "CLEOCATRA", "HOT TO BURN", "HOT TO BURN EXTREME", "JOHN HUNTER AND THE TOMB OF THE SCARAB QUEEN", "JOHN HUNTER AND THE BOOK OF TUT", "JOHN HUNTER AND THE AZTEC TREASURE", "JOHN HUNTER AND THE SECRETS OF DA VINCI'S TREASURE", "GREAT RHINO", "GREAT RHINO MEGAWAYS", "BUFFALO KING", "BUFFALO KING MEGAWAYS", "ZEUS VS HADES GODS OF WAR", "WISDOM OF ATHENA", "PIRATES PUB", "DRAGON HERO", "DRAGON TIGER LUCK", "TREASURE WILD", "GOLD PARTY", "CANDY BLITZ BOMBS", "JUICY FRUITS", "WILD WILD RICHES", "WILD WILD RICHES MEGAWAYS", "3 DANCING MONKEYS", "ANCIENT EGYPT", "ASGARD", "888 DRAGONS", "8 DRAGONS", "7 PIGGIES", "7 MONKEYS", "3 KINGDOMS", "3 GENIE WISHES"]

daftar_noted = ["Gunakan pola saat putaran stabil.", "Perhatikan scatter, jika sering lewat tandanya mesin akan pecah.", "Mainkan kombinasi putaran manual di sela-sela auto spin untuk mengubah acakan server.", "Cari logo scatter 2 berderet, pancing dengan spin manual secara perlahan.", "Jangan terpancing emosi. Jika mesin terasa menyedot, pindah game atau withdraw ya ka.", "Mainkan kombinasi putaran manual di sela-sela auto spin untuk mengubah acakan server.", "Jika dirasa Saldo Sudah menguntungkan, Harap langsung di Withdraw, Utamakan Keuntungan kaka.", "Gunakan teknik gantung spin.", "Coba pancing dengan bet receh dulu sebelum menggunakan pola utama ini.", "Momen gacor biasanya terjadi setelah putaran manual memberikan scatter gratis."]

# --- FUNGSI GENERATOR ---
def buat_pola_pragmatic(nama_game):
    emj = random.choice(["⚡", "🔥", "💫", "💎", "✨"])
    hasil = f"{emj} <b>{nama_game.upper()}</b> {emj}\n\n"
    for _ in range(5):
        hasil += f"{emj} {random.choice([10,20,30,50,70,100])}x {random.choice(['✅','❌'])} {random.choice(['✅','❌'])} {random.choice(['✅','❌'])} {random.choice(['SPIN AUTO', 'SPIN MANUAL'])}\n"
    return hasil + f"\n( Noted )\n{random.choice(daftar_noted)}"

def buat_pola_pgsoft(nama_game):
    emj = random.choice(["🧬", "🐉", "🔥", "🎰", "🍀"])
    hasil = f"{emj} <b>{nama_game.upper()}</b> {emj}\n\n"
    for _ in range(5):
        hasil += f"🎰 {random.choice([10,15,18,21,30,50,100,1000])}x {random.choice(['AUTO SPIN', 'MANUAL TURBO', 'MANUAL SPIN', 'AUTO TURBO'])}\n"
    return hasil + f"\n( Noted )\n{random.choice(daftar_noted)}"

# --- INTERFACE ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🎰 LIST PRAGMATIC", callback_data="menu_pragmatic"), InlineKeyboardButton("🧬 LIST PG SOFT", callback_data="menu_pgsoft"))
    bot.send_message(message.chat.id, "🤖 <b>Bot Pola Gacor SUPERCUAN Ready!</b>\nKetik 'pola nama_game' untuk mulai.", reply_markup=markup, parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    bot.answer_callback_query(call.id)
    if call.data == "menu_pragmatic":
        bot.send_message(call.message.chat.id, "🎰 <b>PRAGMATIC PLAY:</b>\n• " + "\n• ".join(daftar_pragmatic), parse_mode='HTML')
    elif call.data == "menu_pgsoft":
        bot.send_message(call.message.chat.id, "🧬 <b>PG SOFT:</b>\n• " + "\n• ".join(daftar_pgsoft), parse_mode='HTML')
    elif call.data.startswith("acak|"):
        _, prov, game = call.data.split("|")
        pola = buat_pola_pragmatic(game) if prov == "pragmatic" else buat_pola_pgsoft(game)
        bot.edit_message_text(pola, call.message.chat.id, call.message.message_id, reply_markup=pola_keyboard(prov, game), parse_mode='HTML')

def pola_keyboard(prov, game):
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔄 ACAK POLA", callback_data=f"acak|{prov}|{game}"))
    return markup

@bot.message_handler(func=lambda m: m.text.lower().startswith('pola '))
def handle_pola(m):
    game = m.text.replace('pola ', '').strip().upper()
    if game in daftar_pgsoft:
        bot.send_message(m.chat.id, buat_pola_pgsoft(game), reply_markup=pola_keyboard("pgsoft", game), parse_mode='HTML')
    elif game in daftar_pragmatic:
        bot.send_message(m.chat.id, buat_pola_pragmatic(game), reply_markup=pola_keyboard("pragmatic", game), parse_mode='HTML')
    else:
        bot.send_message(m.chat.id, "⚠️ Game tidak ditemukan. Pastikan ketik sesuai list.")

print("Bot sedang berjalan...")
bot.infinity_polling()