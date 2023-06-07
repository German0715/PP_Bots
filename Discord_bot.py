#Mi primer bot de discord! 


#Importando librerías
import discord
from bot_logic import gen_pass  #Para usar esta, debo tener un archivo que se llame bot_logic guardado en la misma carpeta de este archivo



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()

# Activar el privilegio de lectura de mensajes
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


@client.event
async def on_ready():# Este evento se activa cuando el bot se ha conectado exitosamente a Discord y está listo para interactuar.

    print(f'Hemos iniciado sesión como {client.user}') 

@client.event
async def on_message(message): #Este evento se activa cada vez que se recibe un mensaje en un servidor al que el bot tiene acceso
    if message.author == client.user:  #verificamos si el autor es el bot, si si es, no hacemos nada
        return
    if message.content.startswith('$hello'): #Verificamos si el autor somos nosotros, a lo que el bot responderá :) 
        await message.channel.send("Hola, soy un bot!")
    elif message.content.startswith('$bye'):
        await message.channel.send(":confused:")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10)) #El generador de contraseñas! 
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!") 


client.run("MTExNDYwMTAzNTU2MzAxMjE2OA.G4i4Tu.C32773XH7K4vKUg4nD8i4zjuRDjOizPWqw-qFE") # TOKEN --> No borrar 