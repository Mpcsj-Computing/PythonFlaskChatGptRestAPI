from dataclasses import dataclass, field
from typing import Optional

DEFAULT_MODEL = 'text-davinci-003'
DEFAULT_TEMPERATURE = 0.9
DEFAULT_MAX_TOKENS = 1024


@dataclass
class MessageRequestDTO:
    question: str
    max_tokens: Optional[int] = field(default=DEFAULT_MAX_TOKENS)
    temperature: Optional[float] = field(default=DEFAULT_TEMPERATURE)
    model_id: Optional[str] = field(default=DEFAULT_MODEL)

    @staticmethod
    def new_instance_from_flask_body(data: dict) -> 'MessageRequestDTO':
        if 'question' not in data:
            raise Exception('question attribute not found')

        res = MessageRequestDTO(
            question=data['question']
        )

        for attr in ['max_tokens', 'temperature', 'model_id']:
            if attr in data:
                setattr(res, attr, data[attr])
        return res
