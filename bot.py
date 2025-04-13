import discord
from discord.ext import commands
import json
from datetime import datetime

# Getting config information
with open("config.json", "r") as f:
	config = json.loads(f)

intents = discord.Intents.default()
intents.messagee_content = True
bot = commands.Bot(intents=intents)
	

class TwitchIntegrationCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready():
	    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	    print('------')

	@commands.command()
	async def help(ctx, args):
		if len(args) < 1:
			ctx.send("Type '!help [command]' or '!help all' to get help for one or all commands")
			print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !help command called with no parameters")
		else:
			match args[0]:
				case "all":
					ctx.send("\n".join(["## Commdands:",
										"- !so [twitch-username] [options]: shouts out a twitch channel",
										"  - (No Options Currently)",
										"- !ls [twitch-username] [options]: gets the live status of a twitch channel",
										"  - (No Options Currently)"]))
				case "so":
	  				ctx.send("\n".join(["!so [twitch-username] [options]: shouts out a twitch channel",
	  									"  - (No Options Currently)"]))
	  			case "!so":
	  				ctx.send("\n".join(["!so [twitch-username] [options]: shouts out a twitch channel",
	  									"  - (No Options Currently)"]))
	  			case "ls":
	  				ctx.send("\n".join(["!ls [twitch-username] [options]: gets the live status of a twitch channel",
	  									"  - (No Options Currently)"]))
	  			case "!ls":
	  				ctx.send("\n".join(["!ls [twitch-username] [options]: gets the live status of a twitch channel",
	  									"  - (No Options Currently)"]))
	  			case _:
					ctx.send(f"No command found with name \"{args[0]}\"")
			print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !help command called with parameter \"{args[0]}\"")
			
	
	@commands.command()
	async def so(ctx, args):
		if ctx.author.guild_permissions.administrator:
		    if len(args) > 0:
		    	name = args[0]
		    	if len(args) > 1:
			        options = []
			        for i in args[1:]:
			        	pass
			print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !so command called with username \"{username}\"")
	    else:
	    	ctx.send("No Username")
	    	print(datetime.now().toisoformat() + " Guild: " + ctx.guild.name + " | !so command called with no parameters")
	
	@commands.command()
	async def ls(ctx, args):
		if len(args) > 0:
			name = args[0]
			if len(args) > 1:
				options = []
				for i in args[1:]:
					pass
			print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !ls command called with username \"{username}\"")
		else:
			ctx.send("No Username")
			print(datetime.now().toisoformat() + " Guild: " + ctx.guild.name + " | !so command called with no parameters")

channels = ['bot']
bot.add_cog(TwitchIntegrationCog(bot))
bot.run("TOKEN HERE")
