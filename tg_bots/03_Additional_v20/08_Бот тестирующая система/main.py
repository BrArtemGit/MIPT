# https://t.me/YaL_web2_bot

from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from functools import reduce
import random
import json
import copy
import logging

BOT_TOKEN = '7140282622:AAGWSWMVhRhrY3OiT5CK7eA0wQpkeVygI3w'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
TESTFILE = "tests.json"
tests = {}

WAIT_ANSWER = 1

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


async def start(update, context):
    await update.message.reply_text("Пройдите тест. Ответьте на следующие вопросы.")

    # Перемешиваем порядок тестов и запоминаем его для данного пользователя.
    context.user_data["tests"] = copy.deepcopy(tests)
    random.shuffle(context.user_data["tests"])

    # Задаем первый вопрос.
    context.user_data["test_id"] = 0
    await update.message.reply_text(context.user_data["tests"][0]["question"])

    return WAIT_ANSWER


async def stop(update, context):
    await update.message.reply_text("Прерываем тест. До новых встреч!")
    context.user_data.clear()
    return ConversationHandler.END


def count_correct_results(tests):
    # считаем количество правильных ответов.
    return reduce(lambda s, t: s + int(t["correct_answer"]), tests, 0)


async def wait_answer(update, context):
    # Принимаем и проверяем ответ. Записываем флаг корректного ответа в тест.
    response = update.message.text
    test_id = context.user_data["test_id"]
    context.user_data["tests"][test_id]["correct_answer"] = (
            response == context.user_data["tests"][test_id]["response"])

    # Ищем следующий тест. Если еще остались незаданные вопросы -- задаем.
    test_id += 1
    if test_id < len(context.user_data["tests"]):
        context.user_data["test_id"] = test_id
        await update.message.reply_text(context.user_data["tests"][test_id]["question"])
        return WAIT_ANSWER
    # ... в противном случае подводим итоги и сбрасываем данные пользователя.
    else:
        await update.message.reply_text(
            "Правильно: {0} из {1}.".format(count_correct_results(context.user_data["tests"]),
                                            len(context.user_data["tests"])))
        context.user_data.clear()
        return ConversationHandler.END


def main():
    # Загружаем тесты.
    global tests
    with open(TESTFILE, encoding="utf8") as f:
        tests = json.load(f)["test"]

    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            WAIT_ANSWER: [
                MessageHandler(filters.TEXT, wait_answer)
            ]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
