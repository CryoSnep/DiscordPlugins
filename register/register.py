import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
import os
from .utils.chat_formatting import *

class Register:
    """The Register Cog. Also will handle currency/reputation"""

    def __init__(self, bot):
        self.bot = bot
        self.profile = "data/account/accounts.json"
        self.usersArray = dataIO.load_json(self.profile)
    
    @commands.command(name="signup", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _reg(self, ctx, rockstarID : str):
        """Sign up with your SocialClub name to join channels and drops"""
		
		
        server = ctx.message.server
        user = ctx.message.author
        
        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        if user.id not in self.usersArray[server.id]:
			
			#for thisUser in self.usersArray[server.id]
			#	if self.usersArray[server.id][user.id]["SocialClub"] == rockstarID
			#		await self.bot.say("A user has already registered with this SocialClub. Try again.")
			#		return
            self.usersArray[server.id][user.id] = {}
			#self.usersArray[server.id][user.id].update({"SocialClub" : rockstarID})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:", value="You have officially created your account for **{}**, {}.".format(server, user.mention))
            await self.bot.say(embed=data)
        else: 
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Oops, it seems like you already have an account, {}.".format(user.mention))
            await self.bot.say(embed=data)
    @commands.command(name="account", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _acc(self, ctx, user : discord.Member=None):
        """Your/Others Register"""
                    
        server = ctx.message.server
        
        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if not user:
            user = ctx.message.author
            if user.id in self.usersArray[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Age" in self.usersArray[server.id][user.id]:
                    age = self.usersArray[server.id][user.id]["Age"]
                    data.add_field(name="Age:", value=age)
                else:
                    pass
                if "Site" in self.usersArray[server.id][user.id]:
                    site = self.usersArray[server.id][user.id]["Site"]
                    data.add_field(name="Website:", value=site)
                else:
                    pass
                if "About" in self.usersArray[server.id][user.id]:
                    about = self.usersArray[server.id][user.id]["About"]
                    data.add_field(name="About:", value=about)
                else:
                    pass
                if "Gender" in self.usersArray[server.id][user.id]:
                    gender = self.usersArray[server.id][user.id]["Gender"]
                    data.add_field(name="Gender:", value=gender)
                else:
                    pass 
                if "Job" in self.usersArray[server.id][user.id]:
                    job = self.usersArray[server.id][user.id]["Job"]
                    data.add_field(name="Profession:", value=job)
                else:
                    pass
                if "Email" in self.usersArray[server.id][user.id]:
                    email = self.usersArray[server.id][user.id]["Email"]
                    data.add_field(name="Email Address:", value=email)
                else:
                    pass
                if "Other" in self.usersArray[server.id][user.id]:
                    other = self.usersArray[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                prefix = ctx.prefix
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
                await self.bot.say(embed=data)
        else:
            server = ctx.message.server
            if user.id in self.usersArray[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Age" in self.usersArray[server.id][user.id]:
                    town = self.usersArray[server.id][user.id]["Age"]
                    data.add_field(name="Age", value=town)
                else:
                    pass
                if "Site" in self.usersArray[server.id][user.id]:
                    site = self.usersArray[server.id][user.id]["Site"]
                    data.add_field(name="Website:", value=site)
                else:
                    pass
                if "About" in self.usersArray[server.id][user.id]:
                    about = self.usersArray[server.id][user.id]["About"]
                    data.add_field(name="About:", value=about)
                else:
                    pass
                if "Gender" in self.usersArray[server.id][user.id]:
                    gender = self.usersArray[server.id][user.id]["Gender"]
                    data.add_field(name="Gender:", value=gender)
                else:
                    pass 
                if "Job" in self.usersArray[server.id][user.id]:
                    job = self.usersArray[server.id][user.id]["Job"]
                    data.add_field(name="Profession:", value=job)
                else:
                    pass
                if "Email" in self.usersArray[server.id][user.id]:
                    email = self.usersArray[server.id][user.id]["Email"]
                    data.add_field(name="Email Address:", value=email)
                else:
                    pass
                if "Other" in self.usersArray[server.id][user.id]:
                    other = self.usersArray[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="{} doesn't have an account at the moment, sorry.".format(user.mention))
                await self.bot.say(embed=data)

    @commands.group(name="update", pass_context=True, invoke_without_command=True, no_pm=True)
    async def update(self, ctx):
        """Update your TPC"""
        await send_cmd_help(ctx)

    @update.command(pass_context=True, no_pm=True)
    async def about(self, ctx, *, about):
        """Tell us about yourself"""
        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass
        
        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}sign up` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"About" : about})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have updated your About Me to{}".format(about))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def website(self, ctx, *, site):
        """Do you have a website?"""
        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix
        
        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"Site" : site})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Website to {}".format(site))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def age(self, ctx, *, age):
        """How old are you?"""
        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"Age" : age})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your age to {}".format(age))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def job(self, ctx, *, job):
        """Do you have a job?"""
        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"Job" : job})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Job to {}".format(job))
            await self.bot.say(embed=data)
    
    @update.command(pass_context=True, no_pm=True)
    async def gender(self, ctx, *, gender):
        """What's your gender?"""

        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix
                
        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"Gender" : gender})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Gender to {}".format(gender))
            await self.bot.say(embed=data)
 
    @update.command(pass_context=True, no_pm=True)
    async def email(self, ctx, *, email):
        """What's your email address?"""

        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"email" : email})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Email to {}".format(email))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def other(self, ctx, *, other):
        """Incase you want to add anything else..."""
        
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        else:
            pass

        if user.id not in self.usersArray[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            self.usersArray[server.id][user.id].update({"Other" : other})
            dataIO.save_json(self.profile, self.usersArray)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Other to {}".format(other))
            await self.bot.say(embed=data)
    @update.command(pass_context=True, no_pm=True)
    async def _remove(self, ctx, user : discord.Member=None):
        """Remove the specified member from the registry"""
		
        server = ctx.message.server
        if not user		
            user = ctx.message.author
        if server.id not in self.usersArray:
            self.usersArray[server.id] = {}
        if user.id not in self.usersArray[server.id]:
            await self.bot.say("User is not registered")
        else: 
            #self.usersArray[server.id][user.id] = {}
            #self.usersArray[server.id].remove(user.id) 
            #dataIO.save_json(self.profile, self.usersArray)
            #await self.bot.say("removed user")
def check_folder():
    if not os.path.exists("data/account"):
        print("Creating data/account folder...")
        os.makedirs("data/account")

def check_file():
    data = {}
    f = "data/account/accounts.json"
    if not dataIO.is_valid_json(f):
        print("I'm creating the file, so relax bruh.")
        dataIO.save_json(f, data)

def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(Register(bot))
