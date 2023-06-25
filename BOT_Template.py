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

# Crear un bot en la variable cliente y transferirle los privilegios, también se define que el bot funcione con ! 
bot = commands.Bot(command_prefix='!', intents=intents) 

#Para saber si hemos iniciado sesión
@bot.event
async def on_ready():
    print(f"Hemos iniciado sesión como {bot.user}")


#Así se hacen los comandos para que el bot opere
@bot.command()  
async def Micomando(ctx):   #De aquí depende el comando, el nombre que se pone aquí es el comando que el bot usará (!Micomando)
    #AQUÍ VA EL FUNCIONAMIENTO DEL BOT, dependiendo de lo que quieran que haga    
    await ctx.send(loqueenvio)  #acá es lo que el BOT va a responderte cuando escribas !Micomando

#Para correr el BOT
bot.run("YOUR TOKEN HERE") # TOKEN --> No borrar 
