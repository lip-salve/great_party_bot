import common_config

from telegram.ext import Updater, CommandHandler


REQUEST_KWARGS = {
    'proxy_url': common_config.PROXY,
}


def start_message(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Приветули')


def main():
    updater = Updater(common_config.TOCKEN_TELEBOT, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
