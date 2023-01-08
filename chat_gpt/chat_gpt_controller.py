from flask import Blueprint, jsonify, request
from chat_gpt.chat_gpt_service import ChatGptService
from chat_gpt.chat_gpt_model import MessageRequestDTO

chat_gpt_route_path = 'chat-gpt-ai'
chat_gpt_route = Blueprint(chat_gpt_route_path, __name__)


@chat_gpt_route.route("/message", methods=['POST'])
def get_ai_model_answer():
    body = request.json
    return jsonify({
        'result': ChatGptService.get_ai_model_answer(
            MessageRequestDTO.new_instance_from_flask_body(body)
        )
    })


@chat_gpt_route.route('/model')
def get_models():
    return jsonify({
        "models": ChatGptService.list_models()
    })
