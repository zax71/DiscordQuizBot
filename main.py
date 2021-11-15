"""
Discord bot using Pycord for a quiz

GitHub: <when i make it>
Discord: ! Zax71 !#1557

By Zax71
"""

import discord, json

from discord.ui.button import button

secretsFile = open("secrets.json", "r").read()
secrets = json.loads(secretsFile)

secrets["guild"] = int(secrets["guild"])
secrets["user"] = int(secrets["user"])

bot = discord.Bot(
    debug_guild=secrets["guild"]
)

class Buttons(discord.ui.View):
    def init(self):
        super().init()
        self.value = ""

    # When the confirm button is pressed, set the inner value to True and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
    async def buttonA(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        #await interaction.response.send_message("A", ephemeral=True)
        self.value = "A"
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to False
    @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
    async def buttonB(self, button: discord.ui.Button, interaction: discord.Interaction):
        #await interaction.response.send_message("B", ephemeral=True)
        self.value = "B"
        self.stop()
    
    @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
    async def buttonC(self, button: discord.ui.Button, interaction: discord.Interaction):
        #await interaction.response.send_message("C", ephemeral=True)
        self.value = "C"
        self.stop()
    
    @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
    async def buttonD(self, button: discord.ui.Button, interaction: discord.Interaction):
        #await interaction.response.send_message("D", ephemeral=True)
        self.value = "D"
        self.stop()









    @bot.slash_command()  # Quiz1 slash command
    async def quizq1(ctx):
        q1Quiz = discord.Embed(
            title='Question 1',
            description='What is a variable?',
            color=discord.Colour.gold()
            )
        
        q1Quiz.set_footer(text='Discord Quiz Bot')
        q1Quiz.add_field(name="A:", value="A way to store multiple strings that can be edited", inline=False)
        q1Quiz.add_field(name="B:", value="A way to store any kind of data", inline=False)
        q1Quiz.add_field(name="C:", value="A way to store multiple strings that cannot be edited", inline=False)
        q1Quiz.add_field(name="D:", value="A way to store one string", inline=False)
        
        buttons = Buttons()
        await ctx.respond(embed=q1Quiz, view=buttons)
        await buttons.wait()
        if buttons.value == "A":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "B":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "C":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "D":
            await ctx.respond("Incorrect 🙁")
    
    @bot.slash_command()  # Quiz2 slash command
    async def quizq2(ctx):
        q2Quiz = discord.Embed(
            title='Question 1',
            description='What language is interpreted?',
            color=discord.Colour.gold()
            )
        
        q2Quiz.set_footer(text='Discord Quiz Bot')
        q2Quiz.add_field(name="A:", value="Java", inline=False)
        q2Quiz.add_field(name="B:", value="C++", inline=False)
        q2Quiz.add_field(name="C:", value="C#", inline=False)
        q2Quiz.add_field(name="D:", value="Python", inline=False)
        
        buttons = Buttons()
        await ctx.respond(embed=q2Quiz, view=buttons)
        await buttons.wait()
        if buttons.value == "A":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "B":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "C":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "D":
            await ctx.respond("Correct! 🙂")
    
    @bot.slash_command()  # Quiz3 slash command
    async def quizq3(ctx):
        q3Quiz = discord.Embed(
            title='Question 1',
            description='What language is object oriented?',
            color=discord.Colour.gold()
            )
        
        q3Quiz.set_footer(text='Discord Quiz Bot')
        q3Quiz.add_field(name="A:", value="Java", inline=False)
        q3Quiz.add_field(name="B:", value="C++", inline=False)
        q3Quiz.add_field(name="C:", value="C#", inline=False)
        q3Quiz.add_field(name="D:", value="Python", inline=False)
        
        buttons = Buttons()
        await ctx.respond(embed=q3Quiz, view=buttons)
        await buttons.wait()
        if buttons.value == "A":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "B":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "C":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "D":
            await ctx.respond("Incorrect 🙁")

    @bot.slash_command()  # Quiz4 slash command
    async def quizq4(ctx):
        q4Quiz = discord.Embed(
            title='Question 1',
            description='What language is object oriented?',
            color=discord.Colour.gold()
            )
        
        q4Quiz.set_footer(text='Discord Quiz Bot')
        q4Quiz.add_field(name="A:", value="Java", inline=False)
        q4Quiz.add_field(name="B:", value="C++", inline=False)
        q4Quiz.add_field(name="C:", value="C#", inline=False)
        q4Quiz.add_field(name="D:", value="Python", inline=False)
        
        buttons = Buttons()
        await ctx.respond(embed=q4Quiz, view=buttons)
        await buttons.wait()
        if buttons.value == "A":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "B":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "C":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "D":
            await ctx.respond("Incorrect 🙁")

    @bot.slash_command()  # Quiz4 slash command
    async def quizq5(ctx):
        q5Quiz = discord.Embed(
            title='Question 1',
            description='Which of the following are not programing languages?',
            color=discord.Colour.gold()
            )
        
        q5Quiz.set_footer(text='Discord Quiz Bot')
        q5Quiz.add_field(name="A:", value="Java", inline=False)
        q5Quiz.add_field(name="B:", value="HTML", inline=False)
        q5Quiz.add_field(name="C:", value="JavaScript", inline=False)
        q5Quiz.add_field(name="D:", value="CircutPython", inline=False)
        
        buttons = Buttons()
        await ctx.respond(embed=q5Quiz, view=buttons)
        await buttons.wait()
        if buttons.value == "A":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "B":
            await ctx.respond("Correct! 🙂")
        if buttons.value == "C":
            await ctx.respond("Incorrect 🙁")
        if buttons.value == "D":
            await ctx.respond("Incorrect 🙁")

bot.run(secrets["token"])