import time
import telepot
from telepot.loop import MessageLoop
from sklearn.externals import joblib

def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        content = msg["text"]
        # 0 for postive, 1 for negative
        predictions = model.predict([content])
        pos_score = model.predict_proba([content])
        if predictions[0] == 0:
            reply = "This is a positive review!({:.2f})".format(pos_score[0][0])
        if predictions[0] == 1:
            reply = 'This is a negative review!({:.2f})'.format(pos_score[0][0])

        bot.sendMessage(chat_id, reply)

if __name__ == "__main__":

    model = joblib.load('model.pkl')
    # Provide your bot's token
    bot = telepot.Bot("BOT's TOKEN")
    print('bot is ready')
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
