import tweepy
import time

# ===== CONFIGURAÇÃO DAS CREDENCIAIS =====
# Cole aqui o "API Key" que está em "Consumer Keys"
API_KEY = "irn6k6yGqSf1EinQXWY9h1Hz2"

# Cole aqui o "API Secret" que está em "Consumer Keys"
API_SECRET = "es1HLlL0RfougDRXyt566HIF88i2YiQXbPIkFF0RVqAWAPLSpK"

# Cole aqui o "Bearer Token" que está em "Authentication Tokens"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADHZ6gEAAAAAi%2BSQmeV8rx%2B5Omk5FOcpZfDHndk%3DvqYPzYzgRGF7QwQrFb4ykivwGsd9I4pw2jEeLDhgDLNWeAKhFN"

# Cole aqui o "Access Token" que está em "Authentication Tokens"
ACCESS_TOKEN = "2007259782147911680-PcG486EVkAClR1FK8SVMLJKv7ChKed"

# Cole aqui o "Access Token Secret" que está em "Authentication Tokens"
ACCESS_TOKEN_SECRET = "FIp9YQDaQJmdFLyCfB6znwi2zcvduzX5CjuofwtxblW67"
# =========================================

# Autenticação no X (Twitter)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def postar_minutos():
    minutos = 1
    
    while True:
        try:
            # Cria a mensagem
            if minutos == 1:
                mensagem = f"Passou {minutos} minuto"
            else:
                mensagem = f"Passaram {minutos} minutos"
            
            # Posta no X
            client.create_tweet(text=mensagem)
            print(f"✅ Tweet postado: {mensagem}")
            
            # Incrementa o contador
            minutos += 1
            
            # Aguarda 1 minuto (60 segundos)
            time.sleep(60)
            
        except Exception as e:
            print(f"❌ Erro ao postar: {e}")
            time.sleep(60)

if __name__ == "__main__":
    print("🤖 Bot iniciado! Postando a cada 1 minuto...")
    postar_minutos()
