from userbot.database import db
from userbot.modules.word_secret import secret_word

def test_consulta_retorna_string():
    assert isinstance(db.consulta("um teste"), str)
    
def test_chute_correto_retorna_true():
    assert word_secret.verificar_chute("batata") == True
    