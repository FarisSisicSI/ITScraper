import discord
from scraper import NewsScraper


class DiscordBot:
    def __init__(self, token):
        self.token = token

        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents)

        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content == "!it-news":
            await message.channel.send("**Sacekaj, prikupljamo podatke...**")

            scraper = NewsScraper("https://www.itvesti.info/search?max-results=1")
            news_data = scraper.scrape()

            if len(news_data) > 2000:
                for i in range(0, len(news_data), 2000):
                    await message.channel.send(news_data[i:i + 2000])
            else:
                await message.channel.send(news_data)



    def run(self):
        self.client.run(self.token)

