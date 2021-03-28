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

def start(update, context):
    """Send a message when the command /start is issued."""
    file = open('start','r',encoding="utf-8")
    content = file.read()
    file.close()

    kb_start = [
        [InlineKeyboardButton("Кафедра КМАД", callback_data = "about_of_CMAD_departament")],
        [InlineKeyboardButton("Можливості для студентів", callback_data = "opportunities_for_the_student")],
        [InlineKeyboardButton("Умови послугу", callback_data = "conditions_of_entry")]
        ]
 

    reply= InlineKeyboardMarkup(kb_start)

    update.message.reply_text(content, reply_markup = reply)
    url_photo = 'https://cs10.pikabu.ru/post_img/big/2018/12/17/8/1545050459118490544.png'
    update.message.bot.send_photo(chat_id = update.message.chat.id,photo = url_photo)

    

    




def opportunities_for_the_student(update, context):
    text_opportunities_for_the_student= 'У нас є багато цікавих можливостей для студентів. З чого почнемо? '
    kb_opportunities_for_the_student = [
        [InlineKeyboardButton("Практика", callback_data = "practice")] ,
        [InlineKeyboardButton("Проєктне навчання", callback_data = "Project_training")],
        [InlineKeyboardButton("Дуальна освіта", callback_data = "Dual_education")],
        [InlineKeyboardButton("Працевлаштування", callback_data = "Employment")]
        ]
    reply= InlineKeyboardMarkup(kb_opportunities_for_the_student)
    update.callback_query.message.reply_text(text_opportunities_for_the_student, reply_markup = reply)
    
def practice(update, context):
    file = open('practice.txt','r',encoding="utf-8")
    text_practice = file.read()
    file.close()
    
    
    update.callback_query.message.reply_text(text_practice)
    

def Project_training(update, context):
    file = open('Project_training.txt','r',encoding="utf-8")
    text_Project_training = file.read()
    file.close()
    
    update.callback_query.message.reply_text(text_Project_training)
    text = 'https://www.instagram.com/stories/highlights/17864373167331563/'
    update.callback_query.message.reply_text(text)
    

def Dual_education(update, context):
    file = open('Dual_education.txt','r',encoding="utf-8")
    text_Dual_education = file.read()
    file.close()

    update.callback_query.message.reply_text(text_Dual_education)
def Employment(update, context):
    file = open('Employment.txt','r',encoding="utf-8")
    text_Employment = file.read()
    file.close()

    update.callback_query.message.reply_text(text_Employment)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def about_of_CMAD_departament(update, context):
    text_about_of_CMAD_departament= 'З чого почнемо?'
    kb_about_of_CMAD_departament = [
        [InlineKeyboardButton("Викладачі", callback_data = "Teachers")] ,
        [InlineKeyboardButton("Принципи навчання на кафедрі", callback_data = "Principles_of_teaching")],
        [InlineKeyboardButton("Історія кафедри", callback_data = "History_of_the_department")],
        [InlineKeyboardButton('Аудиторії кафедри', callback_data = "Audience_of_the_department")],
        [InlineKeyboardButton('Наші випускники', callback_data = "Our_graduates")]
        ]
    reply= InlineKeyboardMarkup(kb_about_of_CMAD_departament)
    update.callback_query.message.reply_text(text_about_of_CMAD_departament, reply_markup = reply)
        
def Teachers(update, context):
    file = open('Teachers.txt','r',encoding="utf-8")
    text_Teachers = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Teachers)
def Principles_of_teaching(update, context):
    file = open('Principles_of_teaching.txt','r',encoding="utf-8")
    text_Principles_of_teaching = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Principles_of_teaching)
def History_of_the_department(update, context):
    file = open('History_of_the_department.txt','r',encoding="utf-8")
    text_History_of_the_department = file.read()
    file.close()
    update.callback_query.message.reply_text(text_History_of_the_department)
    text = 'https://www.instagram.com/stories/highlights/17859192080412533/'
    update.callback_query.message.reply_text(text)
    
def Audience_of_the_department(update, context):
    file = open('Audience_of_the_department.txt','r',encoding="utf-8")
    text_Audience_of_the_department = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Audience_of_the_department)
    text = 'https://www.instagram.com/stories/highlights/18074436055254149/'
    update.callback_query.message.reply_text(text)
def Our_graduates(update, context):
    file = open('Our_graduates.txt','r',encoding="utf-8")
    text_Our_graduates = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Our_graduates)
    text = 'http://web.kpi.kharkov.ua/kmmm/uk/o_kafedre_ua/nashi-vipuskniki/'
    update.callback_query.message.reply_text(text)
    
    update.message.reply_text()
def ZNO_subjects(update, context):
    file = open('ZNO_subjects.txt','r',encoding="utf-8")
    text_ZNO_subjects = file.read()
    file.close()
    update.callback_query.message.reply_text(text_ZNO_subjects)
def Calculation_of_the_competition(update, context):
    file = open('Calculation_of_the_competition.txt','r',encoding="utf-8")
    text_Calculation_of_the_competition= file.read()
    file.close()
    update.callback_query.message.reply_text(text_Calculation_of_the_competition)
def Stages_of_the_introductory_campaign(update, context):
    file = open('Stages_of_the_introductory_campaign.txt','r',encoding="utf-8")
    text_Stages_of_the_introductory_campaign = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Stages_of_the_introductory_campaign)
    
def Useful_links(update, context):
    file = open('Useful_links.txt','r',encoding="utf-8")
    text_Useful_links = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Useful_links)
def Number_of_bud(update, context):
    file = open('Number_of_bud.txt','r',encoding="utf-8")
    text_Number_of_bud = file.read()
    file.close()
    update.callback_query.message.reply_text(text_Number_of_bud)


def conditions_of_entry(update, context):
    text_conditions_of_entry= 'З чого почнемо?'
    kb_about_of_CMAD_departament = [
        [InlineKeyboardButton("Конкурсні предмети ЗНО", callback_data = "ZNO_subjects")] ,
        [InlineKeyboardButton("Розрахунок конкурсного балу", callback_data = "Calculation_of_the_competition")],
        [InlineKeyboardButton("Етапи вступної кампані", callback_data = "Stages_of_the_introductory_campaign")],
        [InlineKeyboardButton('Корисні посиланн', callback_data = "Useful_links")],
        [InlineKeyboardButton('Кількість бюджетних та контрактних місць для вступників', callback_data = "Number_of_bud")]
        ]
    reply= InlineKeyboardMarkup(kb_about_of_CMAD_departament)
    update.callback_query.message.reply_text(text_conditions_of_entry, reply_markup = reply)
    

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1680692788:AAF4LoU4Kwvmml22f858WuINrwXabOnJgCs", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(about_of_CMAD_departament,pattern = 'about_of_CMAD_departament'))


    dp.add_handler(CallbackQueryHandler(ZNO_subjects,pattern = 'ZNO_subjects'))
    dp.add_handler(CallbackQueryHandler(Calculation_of_the_competition,pattern = 'Calculation_of_the_competition'))
    dp.add_handler(CallbackQueryHandler(Stages_of_the_introductory_campaign,pattern = 'Stages_of_the_introductory_campaign'))
    dp.add_handler(CallbackQueryHandler(Useful_links,pattern = 'Useful_links'))
    dp.add_handler(CallbackQueryHandler(Number_of_bud,pattern = 'Number_of_bud'))



    
    dp.add_handler(CallbackQueryHandler(opportunities_for_the_student,pattern = 'opportunities_for_the_student'))
    dp.add_handler(CallbackQueryHandler(conditions_of_entry,pattern = 'conditions_of_entry'))
    dp.add_handler(CallbackQueryHandler(practice,pattern = 'practice'))
    dp.add_handler(CallbackQueryHandler(Project_training,pattern = 'Project_training'))
    dp.add_handler(CallbackQueryHandler(Dual_education,pattern = 'Dual_education'))
    dp.add_handler(CallbackQueryHandler(Employment,pattern = 'Employment'))

    dp.add_handler(CallbackQueryHandler(Teachers,pattern = 'Teachers'))
    dp.add_handler(CallbackQueryHandler(Principles_of_teaching,pattern = 'Principles_of_teaching'))
    dp.add_handler(CallbackQueryHandler(History_of_the_department,pattern = 'History_of_the_department'))
    dp.add_handler(CallbackQueryHandler(Audience_of_the_department,pattern = 'Audience_of_the_department'))
    dp.add_handler(CallbackQueryHandler(Our_graduates,pattern = 'Our_graduates'))


   




    # on noncommand i.e message - echo the message on Telegram
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

