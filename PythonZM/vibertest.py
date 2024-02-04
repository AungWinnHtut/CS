from viberbot import Api #pip install viberbot
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='https://viber.com/avatar.jpg',
	auth_token='524e6ea27c67d19c-7ecb89e869996967-8ca1582092aa8173'
)
viber = Api(bot_configuration)
print(viber)


