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

@bot.command()
async def consejos(ctx):
    consejos_ambientales=[
        "Apaga las luces cuando salgas de una habitación.",
        "Utiliza bombillas de bajo consumo o LED.",
        "Recicla tus residuos y separa los materiales correctamente.",
        "Usa productos reutilizables en lugar de desechables.",
        "Ahorra agua cerrando el grifo mientras te cepillas los dientes.",
        "Opta por el transporte público o comparte coche para reducir emisiones.",
        "Planta árboles y cuida de los espacios verdes en tu comunidad.",
        "Reduce el consumo de carne y opta por opciones vegetarianas o veganas.",
        "Compra productos locales y de temporada para reducir la huella de carbono del transporte.",
        "Revisa el aislamiento de tu hogar para ahorrar energía en la calefacción o refrigeración."
    ]
    consejo = random.choice(consejos_ambientales)
    await ctx.send(consejo)

# Recordatorios personalizados
@bot.command()
async def recordatorio(ctx, accion):
    await ctx.send(f"Te recordaré {accion} más tarde.")

# Información sobre transporte sostenible
@bot.command()
async def transporte(ctx):
    informacion_transporte = "Aquí tienes información sobre transporte sostenible:\n\n" \
                             "- Rutas de transporte público: [Enlace]\n" \
                             "- Ubicaciones de estaciones de carga para vehículos eléctricos: [Enlace]\n" \
                             "- Alquiler de bicicletas: [Enlace]\n" \
                             "- Consejos para una conducción eficiente: [Enlace]"
    await ctx.send(informacion_transporte)

# Recursos educativos
@bot.command()
async def recursos(ctx):
    recursos_educativos = "Aquí tienes algunos recursos educativos sobre medio ambiente:\n\n" \
                          "- Video: [Enlace]\n" \
                          "- Artículo: [Enlace]\n" \
                          "- Infografía: [Enlace]"
    await ctx.send(recursos_educativos)

# Desafíos y recompensas
@bot.command()
async def desafio(ctx):
    desafio_semanal = "¡Participa en nuestro desafío semanal!\n" \
                      "- Acción: [Descripción de la acción]\n" \
                      "- Recompensa: [Descripción de la recompensa]"
    await ctx.send(desafio_semanal)

bot.run("YOUR TOKEN HERE") # TOKEN --> No borrar 
