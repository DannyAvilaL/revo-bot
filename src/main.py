"""
Programa que realiza la 
"""

import discord
from config import DISCORD_KEY
import sheets

#client = discord.Client()
class RevoBot(discord.Client):

	async def on_ready(self):
		print(f"Sesion iniciada con {self.user}")

	async def on_message(self, mensaje):
		if mensaje.author == self.user:
			return
		if mensaje.content.startswith("$Hola"):
			await mensaje.channel.send("Hola!")

		if mensaje.content == "$Conecta":
			estado = sheets.open_google_sheets()
			await mensaje.channel.send(estado)
		
		if mensaje.content.startswith("$Get"):
			val = sheets.get_cell_value(mensaje.content[5::])
			await mensaje.channel.send(f"Valor de la celda: {val}")

		if mensaje.content.lower().startswith("$nuevo user"):
			await mensaje.channel.send("Ingresa tu nombre completo")


intents = discord.Intents.default()
intents.members = True
bot = RevoBot()
bot.run(DISCORD_KEY)
