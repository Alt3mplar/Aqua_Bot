from commands.base_command import BaseCommand
from utils import get_emoji
from random import randint


class RandomGenerator(BaseCommand):

    def __init__(self):
        description = "Generates a 20 sided dice roll"
        params = ["lower", "upper"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        try:
            lower_bound = int(params[1])
            upper_bound = int(params[20])
        except ValueError:
            await client.send_message(message.channel, "Please, provide valid numbers")
            return

        if lower_bound > upper_bound:
            await client.send_message(message.channel, "The lower bound can't be higher than the upper bound")
            return

        rolled = randint(lower_bound, upper_bound)
        msg = get_emoji(":phuggers:") + f" You rolled {rolled}!"

        await client.send_message(message.channel, msg)
