from discord.ext import commands
import discord
import asyncio
import youtube_dl
import ffmpeg
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)
        await ctx.send(f'Playing: {query}')

    @commands.command()
    async def yt(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        await ctx.send(f'Streaming: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("You are not connected to a voice channel.")
        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Volume set to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

@bot.event
async def on_ready():
    print(f'Te has logueado como el {bot.user}')
    await bot.add_cog(Music(bot))


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
#Así se usa con la clase BOT, el comando es con el prefijo $
@bot.command()
async def hello(ctx):
    await ctx.send(f'¡Hola! Soy un bot de testeo.')
@bot.command()
async def smile(ctx):
    await ctx.send(gen_emodji())
@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())
@bot.command()
async def passw(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def joke(ctx):
    await ctx.send('Había una vez un perro llamado Pegamento: un día Pegamento salió a la calle, se cayó y se pegó')   
@bot.command()
async def git(ctx):
    await ctx.send('https://github.com/Kdekalcio')   
@bot.command()
async def games(ctx):
    await ctx.send('Te recomiendo jugar los siguientes juegos:\n-The Legend of Zelda - Skyward Sword: Un juego de aventura y acción con una increíble historia. Yo jugué a la versión de Wii, pero he escuchado que el remaster de Switch es mejor.\n-Terraria: Un juego de supervivencia y construcción simplemente tremendo, no he jugado mucho porque soy muy malo y tengo poco tiempo, pero siempre es un buen rato cuando lo juego.\n-Dont Starve Together: Juego de supervivencia muy bueno. Recomiendo jugarlo multijugador. Cuando compras la versión de Steam, viene con una copia extra gratis para regalar a un amigo y así jueguen juntos. :> \n-Pokémon Edición Oro HeartGold/Pokémon Edición Plata SoulSilver: Un JRPG por turnos que, como todos los juegos de Pokémon, tiene una *atroz* dificultad para **BEBÉS**, pero tiene un gran post-game (que es prácticamente un segundo juego entero) y es un gran remake en comparación a los originales Oro y Plata. Recomendaría jugarlo después de Rojo/Azul/Amarillo/RojoFuego/VerdeHoja, porque ocurren 3 años después de los recién mencionados y estos hechos de hace 3 años presentan relevancia en la historia.')   
    await ctx.send("-Triangle Strategy: Hecho por Square Enix, lo he visto disponible en Switch y en Steam (a un precio estúpidamente caro). Es un RPG táctico increíble con una increíble historia y, si tienes dudas, puedes jugar una demo gratuita en Switch. También tiene un increíble estilo artístico que me dejó enamorado del juego.\n-Deltarune: Un buen JRPG indie hecho por un buen desarrollador indie. Aún está en desarrollo y solo tiene 2 capítulos finalizados de los 7 que tiene planeados. Está influenciado por Final Fantasy y parcialmente Shin Megami Tensei. Y POR FAVOR DEJEN DE INTENTAR VINCULARLO CON UNDERTALE MALDITA SEA QUE ESTOY CANSADO DE VER A UNDERTALE EN TODOS LADOS DEJEN A DELTARUNE BRILLAR POR SI SOLO.\n-Shin Megami Tensei: Tremenda serie de JRPGs, pero con un giro en las mecánicas: tienes la opción de luchar contra tus enemigos o negociar con ellos para potencialmente reclutarlos y que luchen junto a ti. No estoy seguro, pero yo creo que esta mecánica influenció a Pokémon y Undertale.\n-Doom: Un clásico, todos sabemos qué es Doom en todas sus formas. Después de que implementaron fondos interactivos en Opera GX, espero el día en que alguien sea capaz de correr Doom en uno de esos.\n-Resident Evil 4: Un gran shooter de terror, recuerdo los días cuando con mi hermano jugábamos al original cuando más chicos. Y pensar que ahora le hicieron remake...\n-Final Fantasy VII (el de 1997, no el remake): Gran JRPG que influenció mucho en el género desde su lanzamiento, pero hagas lo que hagas, NUNCA JUEGUES LA TRADUCCIÓN ESPAÑOLA ORIGINAL, ES TERRIBLE, PARECE HECHA CON EL TRADUCTOR DE GOOGLE, MALDITA SEA EQUIPO DE TRADUCCIÓN, ¿DÓNDE ESTÁ MI 'FIESTA'?, ¿POR QUÉ ESTÁN TODOS TAN SERIOS CUANDO SUBO A MI 'FIESTA'?")
@bot.command()
async def books(ctx):
    await ctx.send('Te recomiendo leer los siguiente libros:\n-El Principito: Recuerdo haberlo leído cuando chico, pero no recuerdo nada, pero he escuchado que es bueno así que le creeré a los demás.\n-Charlie y la Fábrica de Chocolate: Un clásico de la literatura, simplemente sublime.\n-Vuelta al Mundo en Ochenta Días: Otro libro del que no me acuerdo porque estaba muy chico, pero recuerdo que me gustaba.\n-La Araña: Un increíble libro que me mantuvo muy pegado a la lectura, los personajes principales y la historia son muy interesantes.\n-Crónica de una Muerte Anunciada: Otro libro que me mantuvo muy suspensivo. El final te lo cuentan desde el comienzo, pero de alguna manera sigue encontrando la forma de mantenerte con esperanza y suspenso hasta el final para ver si el protagonista sobrevive o no.\n-Papelucho: Una serie clásica de la literatura infantil chilena, ¿cómo podrías decirle que no a Papelucho?\n-Quique Hache, detective: Otro clásico de la literatura chilena, me encanta hasta el día de hoy. Debería leerlo de nuevo porque mi memoria se está volviendo borrosa.\n\nEstoy planeando leer 1984 y la trilogía de novelas de Five Nights at Freddys en el futuro. He escuchado cosas buenas, así que supongo que los recomiendo también, aunque yo mismo aún no los haya leído.')   

bot.run('TOKEN HERE')
