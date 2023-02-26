import telebot
import openai

bot_token = '6118773146:AAGXgS_T5ShRt0QzUBY_Wcrdk9iABwG2uic'

bot = telebot.TeleBot(bot_token)

openai.api_key = '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'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, my L❤️ve. You can write your question now!)')


@bot.message_handler(func=lambda message: True)
def answer_question(message):
    print(message.text)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=50,
        temperature=0.9,
        top_p=1.0
    )

    bot.reply_to(message, response['choices'][0]['text'])

    print('-----------------------------------------')

    print(response['choices'][0]['text'])


bot.polling()