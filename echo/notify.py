from echo.uah import BittrexClient
from logging import getLogger
from echo.config import TG_TOKEN
from telegram import Bot

logger = getLogger(__name__)


NOTIFY_PAIR = "USD-BTC"
USER_ID = 562211143


def main():
    client = BittrexClient()

    current_price = client.l_price(pair=NOTIFY_PAIR)

    message = "{} = {}".format(NOTIFY_PAIR, current_price)

    bot = Bot(
         token=TG_TOKEN,
         base_url=locals()
        )
    bot.send_message(
        chat_id=USER_ID,
        text=message,
    )


if __name__ == '__main__':
    main()


