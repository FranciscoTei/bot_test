from modules.start import bot
from modules.secret_word import secret_word
from database import db



bot.send_message("oi")
db.consulta("uma consulta")

secret_word.verificar_chute("planta")