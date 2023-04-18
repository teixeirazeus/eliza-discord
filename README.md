![banner](https://raw.githubusercontent.com/teixeirazeus/eliza-discord/master/readme_assets/banner.png)

O bot Eliza para Discord é um projeto open-source que traz a famosa ELIZA, um dos primeiros chatbots de psicoterapia, para o ambiente do Discord. Eliza foi criada na década de 1960 por Joseph Weizenbaum como um experimento para simular um terapeuta humano. Este projeto adapta o chatbot ELIZA para funcionar no Discord, permitindo que os usuários interajam com a ELIZA por meio de mensagens diretas ou menções em canais de texto.

## Recursos

- Responde às mensagens diretas (DMs)
- Responde a citações e menções do bot em canais de texto
- Baseado no modelo original da ELIZA, com suporte à língua portuguesa

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/teixeirazeus/eliza-discord.git
cd eliza-discord
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Crie um bot no portal do Discord para desenvolvedores e copie o token: https://discord.com/developers/applications

4. Crie um arquivo .env na raiz do projeto e adicione o token do seu bot:

```
TOKEN=YOUR_BOT_TOKEN
```

Substitua YOUR_BOT_TOKEN pelo token do seu bot.

## Execução

Para executar o bot, ative o ambiente virtual e execute o arquivo eliza_bot.py:

```bash
source venv/bin/activate
python eliza_bot.py
```

## Developer

*   Thiago da Silva Teixeira

## License

Released under the [MIT License](http://opensource.org/licenses/MIT).