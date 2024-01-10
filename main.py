from transitions import Machine
import telebot

TOKEN = '6295179051:AAHGTmW9WdvO850ymdsGEEgtc88I71m93zI'
bot = telebot.TeleBot(TOKEN)


class User(object):
    def __init__(self, name):
        self.name = name
        self.machine = Machine(model=self, states=['main_menu', 'women_single', 'men_single', 'next_men',
                                                   'next_women'], initial='main_menu')
        self.machine.add_transition(trigger='welcome', source='*', dest='main_menu')
        self.machine.add_transition(trigger='women_single', source='main_menu', dest='women_single')
        self.machine.add_transition(trigger='men_single', source='main_menu', dest='men_single')
        self.machine.add_transition(trigger='next_men', source='men_single', dest='next_men')
        self.machine.add_transition(trigger='next_women', source='women_single', dest='next_women')


@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Здравствуйте, я чат-бот помощник по хоккею"
                              " Для взаимодействия со мной "
                              "используй следующие команды:\n"
                              "\n /men_single - результаты сокола\n"
                              "/women_single - результаты женской каманды бирюса\n")


@bot.message_handler(commands=['women_single'])
def women_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты женского хоккея:\n\n1 место - Динамо-Нева\n"
                              "2 место - Торнадо\n3 место - Агидель\n\n"
                              "/next_women - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_women'])
def next_women(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Белые Медведицы"
                              "\n5 место - Торнадо"      
                              "\nДля возврата в главное меню используйте /start")


@bot.message_handler(commands=['men_single'])
def men_single(message):
    user_id = message.chat.id
    bot.send_message(user_id, " Результаты мужчин в одиночной разряде:\n\n1 место - Молот\n"
                              "2 место - Зауралье\n3 место - Рубин\n\n"
                              "/next_men - показать 4 и 5 место\n\n"
                              "Для возврата в главное меню используйте /start")


@bot.message_handler(commands=['next_men'])
def next_men(message):
    user_id = message.chat.id
    bot.send_message(user_id, "\n4 место - Химик"                  
                              "\n5 место - Югра"                       
                              "\nДля возврата в главное меню используйте /start")


bot.polling(none_stop=True)