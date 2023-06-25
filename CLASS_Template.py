#Template para que usen con la clase BOT! 

#Importando librerías (se modifica al gusto)

import discord
import requests  #Asegúrese de que tiene instalada la biblioteca requests. Si no es así, ¡instálala con pip install!
from discord.ext import commands
import os
import random
from bot_logic import gen_pass  #Para usar esta, debo tener un archivo que se llame bot_logic guardado en la misma carpeta de este archivo



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

#Para saber si estamos conectados
@client.event
async def on_ready():# Este evento se activa cuando el bot se ha conectado exitosamente a Discord y está listo para interactuar.
    print(f'Hemos iniciado sesión como {client.user}') 


@client.event
async def on_message(message): #Se activa cada vez que se recibe un mensaje (por eso dice on_message y en la función está guardada el mensaje) en un servidor al que el bot tiene acceso
    if message.author == client.user:  #verificamos si el autor es el bot, si si es, no hacemos nada
        return
    if message.content.startswith('$hello'): # Si el mensaje comienza con la palabra $hello 
        await message.channel.send("Hola, soy un bot!") #El bot responderá! 
    elif message.content.startswith('$bye'):
        await message.channel.send(":confused:")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10)) #El generador de contraseñas! 
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!") 


client.run("TOKEN HERE") # TOKEN --> No borrar 
