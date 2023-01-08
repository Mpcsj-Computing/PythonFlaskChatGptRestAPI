from flask import Flask
from chat_gpt.chat_gpt_controller import chat_gpt_route_path, chat_gpt_route

from dotenv import load_dotenv

load_dotenv()

def bootstrap():
    # create app
    app = Flask(__name__)
    # register modules/blueprints
    app.register_blueprint(chat_gpt_route, url_prefix=f'/{chat_gpt_route_path}')
    # start app
    app.run(port=3000, debug=True)


if __name__ == '__main__':
    bootstrap()
