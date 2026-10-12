import telebot
import requests
from db import DB

class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.db = DB("bot_users.db")

    def set_name(self):
        @self.bot.message_handler(commands=["name"])
        def name_handler(message):
            parts = message.text.split()
            if len(parts) < 2:
                self.bot.send_message(message.chat.id, "Напиши: /name Илья")
                return
            self.db.set_name(message.chat.id, parts[1])
            self.bot.send_message(message.chat.id, "Запомнил: " + parts[1])

    def whoami(self):
        @self.bot.message_handler(commands=["whoami"])
        def whoami_handler(message):
            name = self.db.get_name(message.chat.id)
            if name:
                self.bot.send_message(message.chat.id, "Ты " + name)
            else:
                self.bot.send_message(message.chat.id, "Я тебя не знаю. Напиши /name Имя")

    def weather(self):
        @self.bot.message_handler(commands=["weather"])
        def weather_handler(message):
            r = requests.get("https://wttr.in/Lyantor?format=j1")
            data = r.json()
            temp = data["current_condition"][0]["temp_C"]
            self.bot.send_message(message.chat.id, "В Лянторе: " + temp + "°C")

    def run(self):
        self.set_name()
        self.whoami()
        self.weather()
        self.bot.polling()