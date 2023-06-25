

#Mi bot que genera imágenes ! 

#Importando librerías
import discord
import random
import os # Librería OS! 

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

print(len(os.listdir('Memes')))

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}') 

@client.event
async def on_message(message):
    if message.content.startswith('!mem'):
        # Obtener la lista de archivos en la carpeta de imágenes
        image_files = os.listdir('Memes')
        # Seleccionar un archivo aleatorio de la lista
        random_file = random.choice(image_files)
        # Ruta completa del archivo seleccionado
        file_path = os.path.join('Memes', random_file)
        # Abrir el archivo seleccionado
        with open(file_path, 'rb') as f:
            picture = discord.File(f)
        # Enviar el archivo al usuario
        await message.channel.send(file=picture)


bot.run("YOUR TOKEN HERE") # TOKEN --> No borrar 
