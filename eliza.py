import re
import random

from dotenv.main import load_dotenv
import os

load_dotenv()

# Dicionário de respostas
respostas = {
    r"oi|olá|boa\s?(tarde|noite|dia)": [
        "Olá, como posso ajudá-lo hoje?",
        "Oi! Em que posso ajudar?",
    ],
    r"(.*)meu nome é (.*)": ["Prazer em conhecê-lo, {1}. Como posso ajudá-lo hoje?"],
    r"(.*)preciso de ajuda(.*)": [
        "Claro, estou aqui para ajudar. Conte-me mais sobre o que você precisa."
    ],
    r"(.*)triste(.*)": [
        "Sinto muito que você esteja se sentindo triste. O que aconteceu?",
    ],
    r"(.*)feliz(.*)": ["Que bom que você está feliz! O que fez você se sentir assim?"],
    r"(.*)problema(.*)": [
        "Parece que você está passando por um problema. Quer conversar sobre isso?"
    ],
    r"(.*)tchau|adeus(.*)": ["Tchau! Foi bom conversar com você. Até a próxima!"],
    r"(.*)": [
        "Por favor, conte-me mais.",
        "Interessante. Continue.",
        "Entendo. O que mais você gostaria de compartilhar?",
    ],
}


def resposta_eliza(mensagem):
    for padrao, respostas_possiveis in respostas.items():
        match = re.match(padrao, mensagem, re.IGNORECASE)
        if match:
            resposta = random.choice(respostas_possiveis)
            return resposta.format(*match.groups())
    return "Desculpe, não entendi."
