# My_toking_bot
import telebot
from openai import OpenAI

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key="лежит в избранном",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Список для хранения истории разговора
conversation_history = []

# Инициализация Telegram бота
bot = telebot.TeleBot("TOKEN")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Получение текстового сообщения от пользователя
    user_input = message.text

    # Добавление ввода пользователя в историю разговора
    conversation_history.append({"role": "user", "content": user_input})

    try:
        # Отправка запроса в нейронную сеть
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=conversation_history
        )

        # Извлечение и вывод ответа нейронной сети
        ai_response_content = chat_completion.choices[0].message.content
        bot.reply_to(message, "AI: " + ai_response_content)

        # Добавление ответа нейронной сети в историю разговора
        conversation_history.append({"role": "assistant", "content": ai_response_content})

    except Exception as e:
        bot.reply_to(message, "Произошла ошибка: " + str(e))

bot.polling()


