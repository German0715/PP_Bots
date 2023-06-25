#Template para que usen con la clase BOT! 

#Importando librerías (se modifica al gusto)

import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random

#NO BORRAR 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='!', intents=intents)

#Para saber si hemos iniciado sesión
@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")

