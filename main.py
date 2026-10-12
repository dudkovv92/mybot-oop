import os
from dotenv import load_dotenv
from bot import MyBot

load_dotenv()

b = MyBot(os.getenv("TOKEN"))
b.run()