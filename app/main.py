from flask import Flask
from view.chatBotAPI import chatBotAPI
from static.src.rule import getRule

app = Flask(__name__)

app.register_blueprint(chatBotAPI)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
