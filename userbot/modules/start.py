#from pyrogram import Client


class Userbot:
    def __init__(self):
        self.name = "test_bot"
    def send_message(self, text):
        print(f"Enviando mensagem: {text}")
        
bot = Userbot()


