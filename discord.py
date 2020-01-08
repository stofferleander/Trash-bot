import discord
import random
from discord.ext import commands


TOKEN = 'NjY0NDY3OTQ2MzE1MTg2MjA2.XhXgHQ.fnUzprFJRjxAxHlKnDjpVKwhZAM'

#id = 632716862328930314

client = commands.Bot(command_prefix = '!')

@client.command
async def dm(ctx):
    await ctx.author.send('t!trash/8ball og et spørsmål'"\n""t!ping")





@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Min prefix er t! ,  t!Hjelp , Takk for å bruke meg :)"))
    print(f'{client.user.name} is ready')
    print(f'with the id: {client.user.id}')


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} Has left a server')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='👋welcome-goodbyes')
    await channel.send(f'Welcome {member.mention} :grin:')
    role = discord.utils.get(member.guild.roles, name='member')
    await member.add_roles(role)

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='rules')
    await channel.send(f'Bye {member.mention} :disappointed_relieved: ')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'trash'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt',
                 'Yes - definitely.',
                 'you may rely on it.',
                 'As i see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Repy hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'QUESTION: {question }\nANSWER: {random.choice(responses)} ')

@client.command()
@commands.has_permissions(Owner=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")

@client.command()
@commands.has_permissions(Owner=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got ban")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")

@client.command()
@commands.has_permissions(Owner=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to mute people")


@client.command()
@commands.has_permissions(Owner=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Please specify a member")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to unmute people")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def clear(ctx, amount=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    await ctx.channel.purge(limit=amount)

client.run(TOKEN)
