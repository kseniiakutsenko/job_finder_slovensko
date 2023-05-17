import telebot
import massage_contoller
import info_operations

bot = telebot.TeleBot('6132589264:AAHLlhIyNs_onWh4KgyDCvq3MYkJm6UfYuA')


@bot.message_handler(commands=["start", "help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Цей бот займається пошуком роботи в IT сфері.'
                                'Уведіть ваш рівень, бажану посаду та технічні навички й отримайте вакансії.'
                                'Щоб почати, використайте команду "/find_job.')


@bot.message_handler(commands=["find_job"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Чудово. Наш пошук працює в межах Словаччини. Введіть бажане місто. Наприклад, Кошице.')
    with open('data/counter.txt', 'w') as f:
        f.truncate(0)
    with open('data/counter.txt', 'w') as f:
        f.write('4')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    with open('data/counter.txt', 'r') as f:
        counter = int(f.read())
    if counter == 4:
        bot.send_message(message.chat.id,
                         "Чудово! А тепер, будь ласка, введіть ваш професійний рівень. Оберіть trainee, junior, middle чи senior")
        with open('data/counter.txt', 'w') as f:
            f.truncate(0)
        with open('data/counter.txt', 'w') as f:
            f.write('3')
        with open('data/client_info.txt', 'w') as f:
            f.write(str(message.text) + '\n')
    elif counter == 3:
        bot.send_message(message.chat.id,
                         "Тепер введіть, будь ласка, посаду. Наприклад, full-stack java programmer")
        with open('data/counter.txt', 'w') as f:
            f.truncate(0)
        with open('data/counter.txt', 'w') as f:
            f.write('2')
        with open('data/client_info.txt', 'a') as f:
            f.write(message.text + '\n')
    elif counter == 2:
        bot.send_message(message.chat.id,
                         "Ви майже у цілі! Перелічте технічні скілли, якими володієте (декілька ключових) через кому.")
        with open('data/counter.txt', 'w') as f:
            f.truncate(0)
        with open('data/counter.txt', 'w') as f:
            f.write('1')
        with open('data/client_info.txt', 'a') as f:
            f.write(message.text + '\n')
    elif counter == 1:
        bot.send_message(message.chat.id,
                         "Дуже вам дякую! Оброблюю ваш запит на надсилаю список вакансій.")
        with open('data/counter.txt', 'w') as f:
            f.truncate(0)
        with open('data/counter.txt', 'w') as f:
            f.write('0')
        with open('data/client_info.txt', 'a') as f:
            f.write(message.text + '\n')
        try:
            massage_contoller.send_responce()
            bot.send_message(message.chat.id, info_operations.return_vacancies())
        except:
            bot.send_message("Схоже, за вашим запитом поки немає вакансій. Надішліть команду "
                             "/find_job, щоб змінити параметри.")
    else:
        bot.send_message(message.chat.id,
                         "Для початку роботи введіть команду /find_job")


bot.polling(none_stop=True, interval=0)
