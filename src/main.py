import discord

client = discord.Client()

@client.event
async def on_ready():
	print(f"Sesion iniciada con {client.user}")

@client.event
async def on_message(mensaje):
	if mensaje.author == client.user:
		return
	if mensaje.content.startswith("$Hola"):
		await mensaje.channel.send("Hola!")


client.run("")
