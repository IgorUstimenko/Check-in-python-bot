#Основная библиотека, с которой мы работаем
import telebot 
import pprint

# -487497685 - id Конфы
# 638065673 - id Ярослава
# 650687486 - id Игоря
# -1001157407744 - id Канала

TOKEN = '930965434:AAGN6qFMK0Lacu1N-IUu1mc1w-N1JpqpxQo' #Записываем наш основной токен
bot = telebot.TeleBot(TOKEN) #Запихиваем токен в бота

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



yesterday = ''
today = ''
troubles = ''
load = ''
name = ''

@bot.message_handler(commands=['reg']) #? Хендлер для команд
def start(message):
    bot.send_message(message.chat.id, "Чем вы занимались вчера?") #Получаем вчерашние занятия
    bot.register_next_step_handler(message, get_yesterday) #следующий шаг – запись вчерашних занятий

def get_yesterday(message): #получаем занятия на сегодня
    global yesterday
    yesterday = message.text
    bot.send_message(message.chat.id, "Чем будете заниматься сегодня?") #Получаем сегодняшние занятия
    bot.register_next_step_handler(message, get_today)

def get_today(message):
    global today
    today = message.text
    bot.send_message(message.chat.id, "Что может помешать?") #Получаем проблемы
    bot.register_next_step_handler(message, get_troubles)

def get_troubles(message):
    global troubles
    troubles = message.text
    bot.send_message(message.chat.id, "Как нагрузка?") #Получаем уровень нагрузки
    bot.register_next_step_handler(message, get_load)

def get_load(message):
    global load
    global name
    load = message.text
    if message.from_user.id == 650687486:
        name = 'Игорь устименко'
    elif message.from_user.id == 638065673:
        name = 'Гаркуша Ярослав'

    bot.send_message(-1001157407744, name +  '\nЯ вчера ' + yesterday + '\nсегодня я ' + today + '\nпроблемы ' + troubles + '\nзагрузка такая ' + load) 













		

bot.polling()#?Бот слушает, должно так быть всегда

