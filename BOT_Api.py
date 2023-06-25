
#Mi primer bot usando APIs! 

#Importando librerías

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

#El código! 

#Creamos una función que trae las imágenes de patos de la URL 
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


## El código de Pokemon!!! 

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    return None

@bot.command()
async def pokemon(ctx, pokemon_name):
    pokemon_data = get_pokemon_data(pokemon_name)
    if pokemon_data:
        name = pokemon_data["name"]
        base_experience = pokemon_data["base_experience"]
        height = pokemon_data["height"]
        sprite_url = pokemon_data["sprites"]["front_default"]

        response = f"Name: {name}\nBase Experience: {base_experience}\nHeight: {height}"

        await ctx.send(response)
        await ctx.send(sprite_url)
    else:
        await ctx.send(f"Pokemon '{pokemon_name}' not found.")

bot.run("YOUR TOKEN HERE") # TOKEN --> No borrar 
