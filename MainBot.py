import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from db import Database
from PIL import Image
import re
from collections import Counter

TOKEN =""

bot = telebot.TeleBot(TOKEN)
db = Database("bd.db")
rest = Image.open("rest.jpg")
start_png = Image.open("start.png")
test1_png = Image.open("test1.jpg")
test2_png = Image.open("test2.jpg")
test3_png = Image.open("test3.jpg")
test4_png = Image.open("test4.jpg")
test5_png = Image.open("test5.jpg")


@bot.message_handler(commands=['start'])
def start(message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    markupCheck = types.InlineKeyboardMarkup()
    check_but = types.InlineKeyboardButton(text="Начать проходить!", callback_data = "startTest")
    markupCheck.add(check_but)
    chat_id = message.chat.id
    bot.send_photo(chat_id, photo=start_png, caption = "Вашему вниманию предлагается пройти тест, чтобы определить вашу хакерскую касту.Тест состоит из 5 вопросов, ответив на которые вы попадете на самое подходящее для вас направление ИТС ВВГУ с вероятностью 110%.", reply_markup=markupCheck)

def test1(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Да", callback_data = "Yes")
    ot2 = types.InlineKeyboardButton(text="Нет", callback_data = "No")
    markupCheck.add(ot1,ot2)
    bot.edit_message_media(media=InputMediaPhoto(test1_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Когда я покупаю новую технику, я полностью читаю инструкцию, чтобы разобраться со всеми нюансами", reply_markup=markupCheck)   

def test2(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="На структурированность", callback_data = "ot_21")
    ot2 = types.InlineKeyboardButton(text="Красота – главное ", callback_data = "ot_22")
    ot3 = types.InlineKeyboardButton(text="На достоверность информации ", callback_data = "ot_23")
    ot4 = types.InlineKeyboardButton(text="Сделал бы сервер вместо нее ", callback_data = "ot_24")
    markupCheck.add(ot1,ot2,ot3,ot4)
    bot.edit_message_media(media=InputMediaPhoto(test3_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Когда вам необходимо сделать таблицу в excel, на что потратите больше всего времени ?", reply_markup=markupCheck)   

def test3(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Нисколько, это же просто квадрат…", callback_data = "ot_31")
    ot2 = types.InlineKeyboardButton(text=" Зависит от того, кому его предлагать", callback_data = "ot_32")
    ot3 = types.InlineKeyboardButton(text="Я бы отдал/ла за него все деньги ", callback_data = "ot_33")
    ot4 = types.InlineKeyboardButton(text="Больше квадратов, тем больше денег ", callback_data = "ot_34")
    markupCheck.add(ot1,ot2,ot3,ot4)
    bot.edit_message_media(media=InputMediaPhoto(test2_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Сколько по-вашему стоит квадрат Малевича?", reply_markup=markupCheck)   

def test4(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Прилег бы в серверную, там огоньки", callback_data = "ot_41")
    ot2 = types.InlineKeyboardButton(text="В столовую! Взломаю автомат с едой! ", callback_data = "ot_42")
    ot3 = types.InlineKeyboardButton(text="Посчитаю сколько там стоит оборудование ", callback_data = "ot_43")
    ot4 = types.InlineKeyboardButton(text="Напечатаю на 3D принтере кровать ", callback_data = "ot_44")
    markupCheck.add(ot1,ot2,ot3,ot4)
    bot.edit_message_media(media=InputMediaPhoto(test4_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Вы потерялись вечером в офисе GOOGLE. Вам нужно выбрать место, где вы сможете переночевать и дождаться утра. Куда вы пойдете:", reply_markup=markupCheck)   

def test5(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Нарисую точный план офиса на будущее ", callback_data = "ot_51")
    ot2 = types.InlineKeyboardButton(text="Заучу план офиса наизусть (", callback_data = "ot_52")
    ot3 = types.InlineKeyboardButton(text="Попрошу устроить себе собеседование ", callback_data = "ot_53")
    ot4 = types.InlineKeyboardButton(text="Спрошу, что за проводочки у них висят ", callback_data = "ot_54")
    markupCheck.add(ot1,ot2,ot3,ot4)
    bot.edit_message_media(media=InputMediaPhoto(test5_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Вас наконец то вызволили из офиса. Чем же вы займетесь?", reply_markup=markupCheck)   

def end(call):
    ints = Counter(db.count_answers(call.from_user.id)[4:]).most_common(1)[0][0]
    if ints == "1":
        db.update_specialization(call.from_user.id, "Информационные системы и технологии")
    elif ints == "2":
        db.update_specialization(call.from_user.id, "Программная инженерия")
    elif ints == "3":
        db.update_specialization(call.from_user.id, "Прикладная информатика")
    elif ints == "4":
        db.update_specialization(call.from_user.id, "Инфокомуникационные технологии и системы связи")
        
    sp = str(db.count_specialization(call.from_user.id))
    Name = db.count_FIO(call.from_user.id)
    tel = db.count_tele(call.from_user.id)
    
    bot.edit_message_media(media=InputMediaPhoto(start_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption=f"Спасибо что прошел тест\nТебе подойдет спициальность: {sp}\nИмя которое ты нам сказал: {Name}\nТвой телефон: {tel}\nНе забудь подписаться на наш канал тут много интересного https://t.me/itsvvsu")   


def FIO(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Далее", callback_data = "nextfio")
    markupCheck.add(ot1)
    bot.edit_message_media(media=InputMediaPhoto(start_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id = call.message.chat.id, message_id = call.message.id, caption="Давай познакомимся как тебя зовут и какая у тебя фамилия когда напишишь нажми далее", reply_markup=markupCheck)

def error(call):
    bot.edit_message_media(media=InputMediaPhoto(rest), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Похоже ты где-то ошибся попробуй ещё раз")    

def nexttel(call):
    markupCheck = types.InlineKeyboardMarkup(row_width=1)
    ot1 = types.InlineKeyboardButton(text="Далее", callback_data = "next")
    markupCheck.add(ot1)
    bot.edit_message_media(media=InputMediaPhoto(start_png), chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.edit_message_caption(chat_id =call.message.chat.id, message_id = call.message.id, caption="Теперь твой номер телефона что то вроде 89000000000", reply_markup=markupCheck)

@bot.message_handler(content_types=['text'])
def mes(message):
    if re.match(r"^[0-9]{11}$", message.text):
        db.update_tele(message.from_user.id, message.text)
        bot.delete_message(message.chat.id, message.message_id)
        
    elif re.match(r"[а-яА-я]", message.text):
        db.update_fio(message.from_user.id, message.text)
        bot.delete_message(message.chat.id, message.message_id)   
    else:
        bot.delete_message(message.chat.id, message.message_id)
        
        

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "startTest":
            FIO(call)
            
        if call.data == "Yes":
            db.plus_ans(call.from_user.id, "1")
            test2(call)
        if call.data == "No":
            test2(call)
      
      
        if call.data == "ot_21":
            db.plus_ans(call.from_user.id, "1")
            test3(call)
        if call.data == "ot_22":
            db.plus_ans(call.from_user.id, "2")
            test3(call)
        if call.data == "ot_23":
            db.plus_ans(call.from_user.id, "3")
            test3(call)
        if call.data == "ot_24":
            db.plus_ans(call.from_user.id, "4")
            test3(call)


        if call.data == "ot_31":
            db.plus_ans(call.from_user.id, "4")
            test4(call)
        if call.data == "ot_32":
            db.plus_ans(call.from_user.id, "3")
            test4(call)    
        if call.data == "ot_33":
            db.plus_ans(call.from_user.id, "1")
            test4(call)
        if call.data == "ot_34":
            db.plus_ans(call.from_user.id, "2")
            test4(call)

        if call.data == "ot_41":
            db.plus_ans(call.from_user.id, "4")
            test5(call)
        if call.data == "ot_42":
            db.plus_ans(call.from_user.id, "3")
            test5(call)
        if call.data == "ot_43":
            db.plus_ans(call.from_user.id, "1")
            test5(call)
        if call.data == "ot_44":
            db.plus_ans(call.from_user.id, "2")
            test5(call)

        if call.data == "ot_51":
            db.plus_ans(call.from_user.id, "2")
            end(call)
        if call.data == "ot_52":
            db.plus_ans(call.from_user.id, "1")
            end(call)
        if call.data == "ot_53":
            db.plus_ans(call.from_user.id, "3")
            end(call)
        if call.data == "ot_54":
            db.plus_ans(call.from_user.id, "4")
            end(call)
            
        if call.data == "next":
            test1(call)
        
        if call.data == "nextfio":
            nexttel(call)

bot.infinity_polling()
