from database import db

class Secret_Word:
    def __init__(self):
        self.palavras = ["batata", "camaleão", "django", "keiner"]
    def verificar_chute(self, chute):
        if chute in self.palavras:
            print("voce acertou a palavra")
            return True
        return False
            
            
secret_word = Secret_Word()
