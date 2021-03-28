#Подключение библиотек
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import datetime #Библиотека для работы с датой и временем


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


contents = {'start' : {'text' :['data2/start1.txt','data2/start2.txt'],
                       'photo':[],
                       'next_menu': 
                          {'kafedra' : {'text' :['data2/start_kafedra.txt'],
                                        'photo': [],
                                    'next_menu':{ 'vykladachi'  : {'text' : ['data2/start_kafedra_vykladachi_with_url.txt'],
                                                                 'photo': []},
                                                'vidminnosti' : {'text' : ['data2/start_kafedra_vidminnosti.txt'],
                                                                 'photo': []},
                                                'istoria'     : {'text' : ['data2/sstart_kafedra_istoria.txt'],
                                                                 'photo': ['data2/start_kafedra_istoria_urls_photo.txt']},
                                                'auditorii'   : {'text' : ['data2/start_kafedra_auditorii.txt'],
                                                                 'photo': ['data2/start_kafedra_auditorii_urls_photo.txt']},
                                                'vypusnyki'   : {'text' : ['data2/start_kafedra_vypusnyki_with_url.txt'],
                                                                 'photo': []},
                                    }},
                       'mozhlyvosti' :{'text' : ['data2/start_mozhlyvosti.txt'],
                                       'photo': [],
                                    'next_menu': {'proektnnavch'   : {'text': ['data2/start_mozhlyvosti_proektnnavch_with_ulr.txt'],
                                                                    'photo':[]},
                                                'dualosvita'     : {'text': ['data2/start_mozhlyvosti_dualoscita.txt'],
                                                                    'photo':[]},
                                                'pratsevlashuv'  : {'text': ['data2/start_mozhlyvosti_pratsevlashtuv.txt'],
                                                                    'photo':[]},
                                                'praktika'       : {'text': ['data2/start_mozhlyvosti_praktika.txt'],
                                                                    'photo':[]},
                                        }},
                       'umovy'    : {'text' : ['data/start_umovy.txt'],
                                       'photo': [],
                                    'next_menu': {'predmetiZNO'     : {'text': ['data2/start_umovy_predmetiZNO.txt'],
                                                                    'photo':[]},
                                                'rozrakhunokBalu' : {'text': ['data2/start_umovy_rozrakhunokBalu.txt'],
                                                                    'photo':[]},
                                                'etapy'           : {'text': ['data2/start_umovy_etapy.txt'],
                                                                    'photo':[]},
                                                'posylannya'      : {'text': ['data2/start_umovy_posylannya_with_url.txt'],
                                                                    'photo':[]},
                                                'kilkistMists'    : {'text': ['data2/start_umovy_kilkistMists.txt'],
                                                                    'photo':[]},
                                      }}
                     }}
            }



#Универсальная функция для считывания данных с файла file
def read_content_from_file(file):
    global text
    f = open(file, "r", encoding = 'utf-8')
    text = f.read()
    f.close()
 

#Определите несколько обработчиков команд.
#Обычно они требуют два аргумента: update and context.
#Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command /start is issued."""
    file = open('start.txt','r')
    content = file.read()
    file.close()

    kb_start = [
        [InlineKeyboardButton("Кафедра КМАД", callback_data = "about_of_CMAD_departament")],
        [InlineKeyboardButton("Можливості для студентів", callback_data = "opportunities_for_the_student")],
        [InlineKeyboardButton("Умови послугу", callback_data = "conditions_of_entry")]
        ]
 

    reply= InlineKeyboardMarkup(kb_start)

    update.message.reply_text(content, reply_markup = reply)
    
###############################################################
    #Данные о пользователе. Сохраняются в файл users.txt
    user = update.message.from_user
    file = open("users.txt", 'a+') #файл открывается для дозаписи, если нет, то создаёться
    #имя пользователя
    n = user.first_name +' '
    #фамилия пользователя, если отсуцтвует, то пропуск
    n += user.last_name if user.last_name else ''
    
    #name = имя (фамилия) пользователя + id пользователя + дата захода + время захода
    name = n + ' ' + 'id: ' + str(user.id) + ' ' \
           + datetime.datetime.now().strftime("%Y %B %d. %A, %I: %M%p") \
           + ' ' + str(datetime.datetime.now())

    #записываем в файл данные с переменной name и перемещаем курсор на новую строку
    file.write(name + '\n')
    file.close() #закрываем файл
###############################################################
    
    read_content_from_file("data/start.txt") #считывание данных с документа start.txt
    #Сообщение-ответ на текст /start
    update.message.reply_text(text)
    
    #Создание кнопок для быстрого ответа/выбора
    #Создание меню кнопок (список списков кнопок)
    #В один ряд помещаются кнопки помещённые в один список, пример: [[1,2],[3]]
    kb_start = [[InlineKeyboardButton("Кафедра КМАД", \
                                     callback_data = "about_of_CMAD_departament")],\
                [InlineKeyboardButton("Можливості для студентів",\
                                     callback_data = "opportunities_for_the_students")],\
                [InlineKeyboardButton("Умови вступу",\
                                     callback_data = "conditions_of_entry")]\
                ]
    reply = InlineKeyboardMarkup(kb_start)

    read_content_from_file("data/start2.txt") #считывание данных с документа start2.txt
    
    #Прикрипление кнопок к тексту и активация их
    update.message.reply_text(text,reply_markup = reply)
 
#Кафедра КМАД
def about_of_CMAD_departament(update, context):
    read_content_from_file("data/kafedra.txt") #считывание данных с документа kafedra.txt
    #Сообщение-ответ на клик по кнопке "Кафедра КМАД"
    update.callback_query.message.reply_text(text)


#Можливості для студентів
def opportunities_for_the_students(update, context):
    file=open('opportunities_for_the_students','r')
    text_opportunities_for_the_students=file.read()
    file.close()
    kb_opportunities_for_the_students = [
        [InlineKeyboardButton("Практика", callback_data = "practice")] ,
        [InlineKeyboardButton("Проєктне навчання", callback_data = "Project_training")],
        [InlineKeyboardButton("Дуальна освіта", callback_data = "Dual_education")],
        [InlineKeyboardButton("Працевлаштування", callback_data = "Employment")]
        ]
    reply= InlineKeyboardMarkup(kb_opportunities_for_the_student)
    update.callback_query.message.reply_text(text_opportunities_for_the_students, reply_markup = reply)
def practice(update, context):
    file = open('practice.txt','r')
    text_practice = file.read()
    file.close()
    
    
    update.callback_query.message.reply_text(text_practice)
    

def Project_training(update, context):
    file = open('Project training.txt','r')
    text_Project_training = file.read()
    file.close()
    
    update.callback_query.message.reply_text(text_Project_training)
    url_photo = 'https://www.instagram.com/p/CLTrdlfhWIg/'
    update.message.bot.send_photo(chat_id = update.message.chat.id,photo = url_photo)

def Dual_education(update, context):
    file = open('Dual education.txt','r')
    text_Dual_education = file.read()
    file.close()

    update.callback_query.message.reply_text(text_Dual_education)
def Employment(update, context):
    file = open('Employment.txt','r')
    text_Employment = file.read()
    file.close()

    update.callback_query.message.reply_text(text_Employment)    


#Умови вступу
def conditions_of_entry(update, context):
    pass


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

#Функция для отображения всех сообщений пользователя по принципу эхо
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    #Создаём Updater и передаём ему ТОКЕН бота
    #Обязательно установите use_context = True,
    #чтобы использовать новые обратные вызовы на основе контекста
    #Post version 12 this will no longer be necessary
    updater = Updater("1680692788:AAF4LoU4Kwvmml22f858WuINrwXabOnJgCs", use_context=True)


    #Создадим обработчик событий для команд


    #Инициализация диспетчера для регистрации обработчиков
    dp = updater.dispatcher


    #для разных команд - ответы в Телеграм
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    #CallbackQueryHandler  обработчик, который вызывает определенную функцию,
    #если в запросе (Query) находит соответствующий callback_data 
    
    #dp.add_handler(CommandHandler("about_of_CMAD_departament",about_of_CMAD_departament))
    dp.add_handler(CallbackQueryHandler(about_of_CMAD_departament,\
                                       pattern = "about_of_CMAD_departament"))
    dp.add_handler(CallbackQueryHandler(opportunities_for_the_students,pattern = 'opportunities_for_the_students'))
    dp.add_handler(CallbackQueryHandler(practice,pattern = 'practice'))
    dp.add_handler(CallbackQueryHandler(Project_training,pattern = 'Project_training'))
    dp.add_handler(CallbackQueryHandler(Dual_education,pattern = 'Dual_education'))
    dp.add_handler(CallbackQueryHandler(Employment,pattern = 'Employment'))
    
    #Если текст будет написан вне команд - вызовется эхобот Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
