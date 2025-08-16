# Importujemy niezbędne moduły
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Wczytujemy zmienne środowiskowe z pliku .env,
# aby bezpiecznie przechowywać token bota.
load_dotenv()

# Pobieramy token bota ze zmiennej środowiskowej
TOKEN = os.getenv('DISCORD_TOKEN')

# Określamy uprawnienia (intents) dla bota.
# Wymagane do działania komend.
intents = discord.Intents.default()
intents.message_content = True  # Zezwalamy botowi na czytanie zawartości wiadomości.
intents.messages = True
intents.guilds = True

# Tworzymy instancję bota z prefiksem komend (np. !hello)
# i zdefiniowanymi uprawnieniami (intents).
bot = commands.Bot(command_prefix='!', intents=intents)

# Zdarzenie, które uruchamia się, gdy bot jest gotowy.
@bot.event
async def on_ready():
    """Wyświetla informację po połączeniu z Discordem."""
    print(f'Zalogowano jako: {bot.user}')
    print(f'ID Bota: {bot.user.id}')
    print('Bot jest gotowy do pracy!')

# Komenda bota, która odpowiada na polecenie !hello.
@bot.command(name='hello')
async def hello(ctx):
    """
    Komenda, która wysyła powitalną wiadomość.
    Użycie: !hello
    """
    # ctx to kontekst wiadomości, zawiera informacje o kanale, autorze itp.
    await ctx.send(f'Cześć, {ctx.author.name}!')

# Uruchamiamy bota, używając tokenu.
# Pamiętaj, aby token był bezpiecznie przechowywany w pliku .env
# i nigdy nie był umieszczany bezpośrednio w kodzie.
if TOKEN:
    bot.run(TOKEN)
else:
    print("Błąd: Nie znaleziono tokenu w zmiennych środowiskowych. Upewnij się, że plik .env istnieje.")
