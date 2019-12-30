from telegram import Bot
from subprocess import PIPE
from subprocess import Popen
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from echo.config import TG_TOKEN
from echo.uah import BittrexClient
from telegram import Location


def bitcoin_price(bot: Bot, update: Update):
    n_pair= "USD-BTC"
    client = BittrexClient()
    current_price = client.l_price(pair=n_pair)
    message = "{} = {}".format(n_pair, current_price)
    bot.send_message(
            chat_id=update.message.chat_id,
            text=message,
        )


def begin_do(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Greetings!",
    )


def begin_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Я бот, що допоможе дізнатися курс біткойну ",
    )


def begin_time(bot: Bot, update: Update):
    process= Popen("date", stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "error time"
    else:
        text = text.decode("utf-8")
    bot.send_message(
        chat_id=update.message.chat_id,
        text = text,
    )


def echo_d(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Ваше ID НА СЕРВЕРІ - {}\n\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )


def sendloc(bot:Bot, update:Update):
    l = Location(24.245331, 50.400863,)
    bot.send_location(
        chat_id= update.message.chat_id,
        latitude=l.latitude,
        longitude=l.longitude,


    )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,

    )

    bitc_handler = CommandHandler("pricebit", bitcoin_price)
    st_handler = CommandHandler("start", begin_do)
    ms_handler = MessageHandler(Filters.text, echo_d)
    hlp_handler = CommandHandler("help", begin_help)
    time_handler = CommandHandler("time", begin_time)
    loc_handler = CommandHandler("location", sendloc)

    updater.dispatcher.add_handler(bitc_handler)
    updater.dispatcher.add_handler(st_handler)
    updater.dispatcher.add_handler(ms_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(hlp_handler)
    updater.dispatcher.add_handler(loc_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


