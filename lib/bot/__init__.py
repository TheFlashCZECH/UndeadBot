from discord import Intents
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "+"
OWNER_IDS = [830548624126771220]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS, intents=Intents.all(),)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("RUNNING BOT...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("BOT CONNECTED")

	async def on_disconnect(self):
		print("BOT DISCONNECTED")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(830550091239653417) #change it later, this is only for test server, copy server ID
			print("BOT READY")

		else:
			print("BOT RECONNECTED")

	async def on_message(self, message):
		pass


bot = Bot()