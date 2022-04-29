"""
Main code that runs the discord bot into the server
This bot main purpose is filtering the un-wanted access
"""

import discord
from config import DISCORD_KEY, MENSAJE_BIENVENIDA
import sheets
import re

intents = discord.Intents.all() #.default()
intents.members = True

class RevoBot(discord.Client):

	def __init__(self):
		super().__init__(intents = intents)
		self.unregistered = "sin verificar"
		self.registered = "blue"

	students = {}

	async def on_ready(self):
		"""
		Function that prints the info into the terminal
		to let the owner that is initialized
		"""
		print(f"Sesion iniciada con {self.user}")
		self.channel_id = 921902844444049470
		self.channel_name = "revo-bot"
	

	async def on_member_join(self, member):
		"""
		For every member joined into the server,
		send a DM message sending the welcome message.
		"""
		print(f"{member.name} se unió")
		await member.add_roles(discord.utils.get(member.guild.roles, name=self.unregistered))
		channel = await member.create_dm()
		await channel.send(MENSAJE_BIENVENIDA)
		await channel.send("Por favor ingresa tu matrícula")

		def esperar_matricula(msg) -> any:
			"""
			Check that the id is valid with regex
			add the value into the Student class

			Returns if valid: discord.message.Message
			Returns if not valid: any
			"""
			valid = bool(re.match(r"A\d{8}", msg.content))
			return valid and msg.channel == channel 

		def esperar_nombre(msg) -> any:
			"""
			Waits until a name is sent
			Accepts only name characters.
			Prevents getting spam or invalid data
			"""
			valid = bool(re.match(r"[^0-9*.$+-=!@~^!¡?¿%&/()]{7,30}", msg.content))
			return valid and msg.channel == channel

		msg = await self.wait_for('message', check=esperar_matricula)
		matricula = msg.content
		self.students[msg.author.id] = {'matricula': matricula}
		await msg.add_reaction("✌")
		#add typing delay
		await channel.trigger_typing() #-> not in class
		await channel.send("Por favor ingresa tu nombre completo")
		msg = await self.wait_for('message', check=esperar_nombre)
		self.students[msg.author.id]['Nombre'] = msg.content
		await msg.add_reaction("✌")
		author_id = msg.author.id
		member = self.guild.get_member(msg.author.id)
		await member.add_roles(discord.utils.get(member.guild.roles, name=self.registered))
		await member.remove_roles(discord.utils.get(member.guild.roles, name=self.unregistered))
		await channel.send("En caso de no tener tu nuevo rol contacta a un administrador.")
		

	async def on_message(self, mensaje):
		if mensaje.author == self.user:
			return

		# Agregar privilegios a propietario de bot unicamente
		if mensaje.content.startswith("$Config"):
			self.channel_id = mensaje.channel.id
			self.channel_name = mensaje.channel.name
			self.guild = mensaje.guild
			self.server = mensaje.guild
			estado = sheets.open_google_sheets()
			await mensaje.add_reaction(f"<:hehe:960943492392165376>")
			await mensaje.channel.send("Bot Configurado")
			await mensaje.channel.send(estado)

		if mensaje.content == "$registro" and mensaje.guild.id == self.server.id:
			await mensaje.channel.send("Te enviaremos un DM.")
			channel = await mensaje.author.create_dm()
			await channel.send(MENSAJE_BIENVENIDA)
			self.temp_channel = mensaje.channel
			await channel.send("Por favor ingresa tu matrícula")

			def esperar_matricula(msg) -> any:
				"""
				Check that the id is valid with regex
				add the value into the Student class

				Returns if valid: discord.message.Message
				Returns if not valid: any
				"""
				valid = bool(re.match(r"A\d{8}", msg.content))
				return valid and msg.channel == channel 

			def esperar_nombre(msg) -> any:
				"""
				Waits until a name is sent
				Accepts only name characters.
				Prevents getting spam or invalid data
				"""
				valid = bool(re.match(r"[^0-9*.$+-=!@~^!¡?¿%&/()]{7,30}", msg.content))
				return valid and msg.channel == channel

			msg = await self.wait_for('message', check=esperar_matricula)
			matricula = msg.content
			self.students[msg.author.id] = {'matricula': matricula}
			await msg.add_reaction("✌")
			#add typing delay
			await channel.trigger_typing()
			await channel.send("Por favor ingresa tu nombre completo")
			msg = await self.wait_for('message', check=esperar_nombre)
			self.students[msg.author.id]['Nombre'] = msg.content
			await msg.add_reaction("✌")
			author_id = msg.author.id
			member = self.guild.get_member(msg.author.id)
			await member.add_roles(discord.utils.get(member.guild.roles, name=self.registered))
			await member.remove_roles(discord.utils.get(member.guild.roles, name=self.unregistered))

		# Might improve to give more random and funny messages
		if mensaje.content.startswith("$Hola"):
			await mensaje.channel.send("Hola!")
		
		if mensaje.content.startswith("$Get"):
			val = sheets.get_cell_value(mensaje.content[5::])
			await mensaje.channel.send(f"Valor de la celda: {val}")

		if mensaje.content.lower().startswith("$nuevo user"):
			await mensaje.channel.send("Ingresa tu nombre completo")
		
		if mensaje.content.lower() == "$mimir":
			await mensaje.channel.send(f"Hora de ir a mimir <:hehe:960943492392165376>")
			await self.close()
			exit()


bot = RevoBot()
bot.run(DISCORD_KEY)
