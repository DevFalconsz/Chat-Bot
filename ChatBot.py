from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("IA:")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.portuguese.greetings",
              "chatterbot.corpus.portuguese.conversations")

print("\033[;1m"+"\033[0;32m"+"  _____  _             _    ____          _")
print("\033[;1m"+"\033[0;32m"+" / ____|| |           | |  |  _ \        | |")
print("\033[;1m"+"\033[0;32m"+"| |     | |__    __ _ | |_ | |_) |  ___  | |_")
print("\033[;1m"+"\033[0;32m"+"| |     | '_ \  / _` || __||  _ <  / _ \ | __|")
print("\033[;1m"+"\033[0;32m"+"| |____ | | | || (_| || |_ | |_) || (_) || |_")
print("\033[;1m"+"\033[0;32m"+" \_____||_| |_| \__,_| \__||____/  \___/  \__|")

print("")

while True:
    user_input = input('\033[34m'+'Você: ')
    response = chatbot.get_response(user_input)
    print('\033[31m'+'Chatbot:', response)