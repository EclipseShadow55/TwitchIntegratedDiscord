"""
Copyright 2025 EclipseShadow55 (https://github.com/EclipseShadow55)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import discord
from discord.ext import commands
from commands import Cog, CheckFailure
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# Getting config information
with open("config.json", "r") as f:
	config = json.load(f)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents)
	
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(description="Sends the bot's latency")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}")

so_opts = {"no-link": "Removes the link to the channel from the bot's reply",
           "no-thumb": "Removes the thumbnail (if the channel is live) from the bot's reply",
           "no-status": "Removes the live status from the bot's reply",
           "no-bio": "Removes the channel's bio from the bot's reply",
          }

status_opts = {"no-link": "Removes the link to the channel from the bot's reply",
               "no-thumb": "Removes the thumbnail (if the channel is live) from the bot's reply"

so_desc = ["`/so [twitch-username] [options]`: shouts out a twitch channel",
           "  Options:"] + \
          ["  - `" + key + "`: " + so_opts[key] for key in so_opts]

status_desc = ["`/status [twitch-username] [options]`: gets the live status of a twitch channel",
               "  Options:"] + \
              ["  - `" + key + "`: " + status_opts[key] for key in status_opts]

all_desc = ["## Commands:"] + \
           ["  - " + so_desc[0]] + \
           ["  " + item for item in so_desc[1:]] + \
           ["  - " + ls_desc[0]] + \
           ["  " + item for item in status_desc[1:]]

class TwitchIntegrationCog(Cog):
	def __init__(self, bot):
		self.bot = bot
    
	@commands.slash_command("Command descriptions and info")
    @discord.option("command", type=str, choices=["all", "/so", "/status"], default="all")
	async def help(ctx, command: str):
        match command:
            case "all":
                ctx.send("\n".join(all_desc))
            case "/so":
                ctx.send("\n".join(so_desc))
            case "/status":
                ctx.send("\n".join(status_desc))
            case _:
                ctx.send(f"No command found with name \"{args[0]}\"")
        print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !help command called with parameter \"{command}\"\n")
			
	@commands.slash_command("Shouts out a twitch channel")
	@discord.option("username", type=str, description="The twitch channel to shoutout")
    @discord.option("options", type=str, description="\n".join(["One or more of these seperated by spaces:",
                                                                ",".join([key for key in so_opts]),
                                                                "`/help /so` for more info"]),
                    default="")
    commands.is_admin()
	async def so(ctx, username: str, options: str):
        options = [item for item in options.split() if item in so_opts]
        # TODO: Implement logic for getting stream / channel info
        print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !so command called with username \"{username}\" and options \"{options}\"\n")
	
	@commands.slash_command(description="Checks the live status of a twitch channel")
    @discord.option("username", type=str, description="The twitch channel to check the live-status of")
    @discord.option("options", type=str, description="\n".join(["One or more of these seperated by spaces:",
                                                                ",".join([key for key in status_opts]),
                                                                "`/help /status` for more info"]),
                    default="")
    commands.is_admin()
	async def status(ctx, username: str, options: str):
		options = [item for item in options.split() if item in status_opts]
        # TODO: Implement logic for getting channel status
		print(f"{datetime.now().toisoformat()} Guild: {ctx.guild.name} | !ls command called with username \"{username}\" and options \"{options}\"\n")

bot.add_cog(TwitchIntegrationCog(bot))
bot.run(os.getenv("TOKEN"))
